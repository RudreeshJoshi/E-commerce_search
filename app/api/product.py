from fastapi import APIRouter, HTTPException
from app.models.product import ProductCreate, ProductMetadata
from app.services.catalog import catalog

router = APIRouter()

@router.post("/product")
def create_product(req: ProductCreate):
    return {"productId": catalog.add_product(req)}

@router.put("/product/meta-data")
def update_metadata(req: ProductMetadata):
    product = catalog.update_metadata(req.productId, req.metadata)
    if not product:
        raise HTTPException(404, "Product not found")
    return product
