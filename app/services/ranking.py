from rapidfuzz import fuzz
import time

def rank_products(query: dict, products: list):
    def score(p):
        text = fuzz.partial_ratio(
            query["normalized"],
            f"{p.title} {p.description}"
        ) / 100

        intent = 0
        if query["cheap"] and p.price < 50000:
            intent += 1
        if query["latest"]:
            intent += 1 / (time.time() - p.created_at + 1)
        if query["accessory"] and "cover" in p.title.lower():
            intent += 1

        business = (
            (p.rating / 5) * 0.4 +
            min(p.units_sold / 10000, 1) * 0.3 +
            (1 if p.stock > 0 else 0) * 0.3
        )

        price_fit = 1 if not query["price_cap"] or p.price <= query["price_cap"] else 0

        return (
            0.4 * text +
            0.2 * intent +
            0.2 * business +
            0.2 * price_fit
        )

    return sorted(products, key=score, reverse=True)[:20]
