from fastapi import FastAPI
from app.api import product, search

app = FastAPI(title="Ecommerce Search Service")

app.include_router(product.router, prefix="/api/v1")
app.include_router(search.router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
