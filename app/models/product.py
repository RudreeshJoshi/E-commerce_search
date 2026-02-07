from pydantic import BaseModel
from typing import Dict
import time
import uuid

class ProductCreate(BaseModel):
    title: str
    description: str
    rating: float
    stock: int
    price: int
    mrp: int
    currency: str = "INR"

class ProductMetadata(BaseModel):
    productId: str
    metadata: Dict[str, str]

class Product(BaseModel):
    id: str
    title: str
    description: str
    rating: float
    stock: int
    price: int
    mrp: int
    currency: str
    units_sold: int
    created_at: float
    metadata: Dict[str, str]

    @staticmethod
    def create(req: ProductCreate):
        return Product(
            id=str(uuid.uuid4()),
            title=req.title,
            description=req.description,
            rating=req.rating,
            stock=req.stock,
            price=req.price,
            mrp=req.mrp,
            currency=req.currency,
            units_sold=0,
            created_at=time.time(),
            metadata={}
        )
