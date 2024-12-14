from enum import Enum
from fastapi import FastAPI, Query, HTTPException, status
from storage import storage
from pydantic import BaseModel, Field

app = FastAPI(description="Travel website")


class ResortClass(str, Enum):
    ECONOMY = "economy"
    STANDARD = "standard"
    COMFORT = "comfort"
    ALL_INCLUSIVE = "all_inclusive"
    VIP = "vip"


class NewOffer(BaseModel):
    country: str
    city: str
    price: float = Field(default=1000, gt=100)
    photo: str
    tags: list[ResortClass] = Field(default=[])
    description: str


class SavedOffer(NewOffer):
    id: str = Field(example="31c77035c9f44bd580c69b3b100f9e03")


@app.get("/")
def index():
    return {"status": "API is working"}


@app.post("/api/create", status_code=status.HTTP_201_CREATED, response_model=SavedOffer)
def create_offer(offer: NewOffer):
    created_offer = storage.create_offer(offer.dict())
    return created_offer


@app.get("/api/get-offers/", response_model=list[SavedOffer])
def get_offers(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, gt=0),
    search_param: str = "",
):
    offers = storage.get_offers(skip, limit, search_param)
    return offers


@app.get("/api/get-offers/{offer_id}", response_model=SavedOffer)
def get_offer(offer_id: str):
    offer = storage.get_offers_info(offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer


@app.delete("/api/delete-offers/{offer_id}", status_code=status.HTTP_200_OK)
def delete_offer(offer_id: str):
    try:
        storage.delete_offers(offer_id)
        return {"status": "deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Offer not found")


@app.patch("/api/update-offers/{offer_id}", response_model=SavedOffer)
def update_offer(offer_id: str, updated_data: NewOffer):
    try:
        updated_offer = storage.update_offers(offer_id, **updated_data.dict())
        return updated_offer
    except ValueError:
        raise HTTPException(status_code=404, detail="Offer not found")
