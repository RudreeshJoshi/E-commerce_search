import json
import random

products = []
for i in range(1200):
    products.append({
        "title": f"Iphone {random.randint(10,16)}",
        "description": "Apple smartphone",
    })

with open("data/raw/scraped_products.json", "w") as f:
    json.dump(products, f)
