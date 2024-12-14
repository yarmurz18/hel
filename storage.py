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
    def get_offer_info(self, offer_id: str):
        pass

    @abstractmethod
    def update_offer(self, offer_id:str, country: str):
        pass

    @abstractmethod
    def delete_offer(self, offer_id: str):
        pass


class JSONStorage(BaseStorage):
    def __init__(self):
        self.__file_name = "storage.json"
        my_file = Path(self.__file_name)
        if not my_file.is_file():
            with open(self.__file_name, mode="w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

    def create_offer(self, offer: dict):
        with open(self.__file_name, mode="r", encoding="utf-8") as file:
            content: list[dict] = json.load(file)

        offer["id"] = uuid4().hex
        content.append(offer)
        with open(self.__file_name, mode="w", encoding="utf-8") as file:
            json.dump(content, file, indent=4)
        return offer

    def get_offers(self, skip: int = 0, limit: int = 15, search_param: str = ""):
        with open(self.__file_name, mode="r", encoding="utf-8") as file:
            content: list[dict] = json.load(file)

        if search_param:
            content = [offer for offer in content if search_param.lower() in offer["country"].lower()]
        return content[skip: skip + limit]

    def get_offer_info(self, offer_id: str):
        with open(self.__file_name, mode="r", encoding="utf-8") as file:
            content: list[dict] = json.load(file)

        for offer in content:
            if offer["id"] == offer_id:
                return offer
        return None

    def update_offer(self, offer_id: str, **kwargs):
        with open(self.__file_name, mode="r", encoding="utf-8") as file:
            content: list[dict] = json.load(file)

        for offer in content:
            if offer["id"] == offer_id:
                for key, value in kwargs.items():
                    if key in offer:
                        offer[key] = value
                with open(self.__file_name, mode="w", encoding="utf-8") as file:
                    json.dump(content, file, indent=4)
                return offer
        raise ValueError(f"Offer with ID {offer_id} not found")

    def delete_offer(self, offer_id: str):
        with open(self.__file_name, mode="r", encoding="utf-8") as file:
            content: list[dict] = json.load(file)

        updated_content = [offer for offer in content if offer["id"] != offer_id]
        if len(updated_content) < len(content):
            with open(self.__file_name, mode="w", encoding="utf-8") as file:
                json.dump(updated_content, file, indent=4)
            return True
        raise ValueError(f"Offer with ID {offer_id} not found")


storage = JSONStorage()


