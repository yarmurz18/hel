import json
from abc import ABC, abstractmethod
from pathlib import Path
from uuid import uuid4


class BaseStorage(ABC):

    @abstractmethod
    def create_offer(self, offer: dict):
        pass

    @abstractmethod
    def get_offers(self, skip: int = 0, limit: int = 15, search_param: str = ""):
        pass

    @abstractmethod
    def get_offers_info(self, offer_id: str):
        pass

    @abstractmethod
    def update_offers(self, offer_id:str, country: str):
        pass

    @abstractmethod
    def delete_offers(self, offer_id: str):
        pass


class JSONStorage(BaseStorage):
    def __init__(self):
        self.file_name = "storage.json"

        my_file = Path(self.file_name)
        if not my_file.is_file():
            with open(self.file_name, mode="w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

    def create_offer(self, offer: dict):
        with open(self.file_name, mode="r") as file:
            content: list[dict] = json.load(file)

        offer["id"] = uuid4().hex
        content.append(offer)
        with open(self.file_name, mode="w", encoding="utf-8") as file:
            json.dump(content, file, indent=4)

    def get_offers(self, skip: int = 0, limit: int = 15, search_param: str = ""):
        with open(self.file_name, mode="r") as file:
            content: list[dict] = json.load(file)

        if search_param:
            data = []
            for offer in content:
                if search_param in offer["country"]:
                    data.append(offer)
            sliced = data[skip:][limit:]
            return sliced

        sliced = content[skip:][limit:]
        return sliced

    def get_offers_info(self, offer_id: str):
        with open(self.file_name, mode="r") as file:
            content: list[dict] = json.load(file)
        for offer in content:
            if offer_id == offer["id"]:
                return offer
        return {}

    def update_offers(self, offer_id: str, country: str):
        with open(self.file_name, mode="r") as file:
            content: list[dict] = json.load(file)
        was_found = False
        for offer in content:
            if offer_id == offer["id"]:
                offer["country"] = country
                was_found = True
                break
        if  was_found:
            with open(self.file_name, mode="w", encoding="utf-8") as file:
                json.dump(content, file, indent=4)
        raise ValueError

    def delete_offers(self, offer_id: str):
        with open(self.file_name, mode="r") as file:
            content: list[dict] = json.load(file)
        was_found = False
        for offer in content:
            if offer_id == offer["id"]:
                content.remove(offer)
                was_found = True
                break
        if was_found:
            with open(self.file_name, mode="w", encoding="utf-8") as file:
                json.dump(content, file, indent=4)
        raise ValueError


storage = JSONStorage()


