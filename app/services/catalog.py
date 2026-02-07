from typing import Dict, List
from app.models.product import Product, ProductCreate

class Catalog:
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, req: ProductCreate) -> str:
        product = Product.create(req)
        self.products[product.id] = product
        return product.id

    def update_metadata(self, product_id: str, metadata: Dict):
        product = self.products.get(product_id)
        if not product:
            return None
        product.metadata.update(metadata)
        return product

    def list_products(self) -> List[Product]:
        return list(self.products.values())

catalog = Catalog()
