from fastapi import APIRouter, Query
from app.services.catalog import catalog
from app.services.ranking import rank_products
from app.services.query_parser import parse_query

router = APIRouter()

@router.get("/search/product")
def search_products(query: str = Query(...)):
    parsed = parse_query(query)
    products = catalog.list_products()
    ranked = rank_products(parsed, products)
    return {"data": ranked}
