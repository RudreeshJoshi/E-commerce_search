import re

HINGLISH = {
    "sasta": "cheap",
    "sastha": "cheap",
    "mehnga": "expensive"
}

def parse_query(query: str) -> dict:
    q = query.lower()
    for k, v in HINGLISH.items():
        q = q.replace(k, v)

    price_cap = None
    match = re.search(r'(\d+)\s*(k|rs|rupees)?', q)
    if match:
        price_cap = int(match.group(1))
        if match.group(2) == "k":
            price_cap *= 1000

    return {
        "raw": query,
        "normalized": q,
        "price_cap": price_cap,
        "cheap": "cheap" in q,
        "latest": "latest" in q,
        "accessory": any(x in q for x in ["cover", "case", "charger"])
    }
