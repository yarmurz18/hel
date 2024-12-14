from fastapi import FastAPI, Query, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from storage import storage
from pydantic import BaseModel, Field
from typing import Annotated
from enum import Enum


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

app = FastAPI(description="travel website")

class Resort_class(str, Enum):
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
    tags: list[Resort_class] = Field(default=[])
    description: str

class SavedOffer(NewOffer):
    id: str = Field(examples=["31c77035c9f44bd580c69b3b100f9e03"])

fake_db_users = [
    {"username": "alex", "password": "admin", "is_admin": True, "token": "31c77035c9f44bd580c69b3b100f9e03"},
    {"username": "alice", "password": "secret", "is_admin": False, "token": "31c77035c9f44bd580c69b3b100f8e02"},
]

class User(BaseModel):
    username: str
    is_admin: bool
    token: str
    password: str

@app.post("/api/token")
def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> dict:
    for user in fake_db_users:
        if user["username"] == form_data.username and user["password"] == form_data.password:
            return {"access_token": user["token"], "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    for user in fake_db_users:
        if user["token"] == token:
            return User(**user)
    raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/api/create", status_code=status.HTTP_201_CREATED)
def create_offer(offer: NewOffer, current_user: User = Depends(get_current_user)) -> SavedOffer:
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin rights required")
    created_offer = storage.create_offer(offer.dict())
    return SavedOffer(**created_offer)

@app.get("/api/get-offers/")
def get_offers(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, gt=0),
    search_param: str = "",
    current_user: User = Depends(get_current_user),
) -> list[SavedOffer]:
    offers = storage.get_offers(skip, limit, search_param)
    return [SavedOffer(**offer) for offer in offers]

@app.get("/api/get-offers/{offer_id}")
def get_offer(offer_id: str, current_user: User = Depends(get_current_user)) -> SavedOffer:
    offer = storage.get_offer_info(offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return SavedOffer(**offer)

@app.delete("/api/get-offers/{offer_id}")
def delete_offer(offer_id: str, current_user: User = Depends(get_current_user)) -> dict:
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin rights required")
    storage.delete_offer(offer_id)
    return {"detail": "Offer deleted"}

@app.patch("/api/get-offers/{offer_id}")
def update_offer(offer_id: str, updates: dict, current_user: User = Depends(get_current_user)) -> SavedOffer:
    updated_offer = storage.update_offer(offer_id, **updates)
    return SavedOffer(**updated_offer)
