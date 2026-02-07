import json
import random

with open("data/raw/scraped_products.json") as f:
    raw = json.load(f)

for p in raw:
    p.update({
        "rating": round(random.uniform(3.5, 4.8), 1),
        "stock": random.randint(0, 100),
        "price": random.randint(30000, 120000),
        "mrp": random.randint(40000, 130000),
        "units_sold": random.randint(0, 10000)
    })

with open("data/processed/catalog_seed.json", "w") as f:
    json.dump(raw, f)
