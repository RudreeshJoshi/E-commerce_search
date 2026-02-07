# E-Commerce Search Engine (MVP)

A search and ranking microservice for an e-commerce platform focused on electronics, optimized for Tier-2 and Tier-3 cities in India.

The system supports typo-tolerant search, Hinglish queries, price-sensitive ranking, and business-aware relevance scoring.

---

## Problem Statement

In a large electronics catalog (millions of products), users often search using:
- Typos (e.g. `Ifone 16`)
- Hinglish queries (e.g. `Sasta iPhone`)
- Price constraints (e.g. `iPhone 50k rupees`)
- Attribute intent (e.g. color, storage, accessories)

The goal is to return **relevant and affordable products**, ranked intelligently and within **<1000ms latency**.

---

## Architecture

- **FastAPI** microservice
- **In-memory catalog** (for low latency)
- Modular layers:
  - API layer (`app/api`)
  - Business logic (`app/services`)
  - Models (`app/models`)
- Easily extensible to Elasticsearch / datastore later

---

## Ranking Strategy (Core Design)

The ranking algorithm is **hybrid and explainable**:

1. **Text relevance**
   - Fuzzy matching (RapidFuzz)
   - Handles typos and partial matches

2. **Query intent**
   - Hinglish normalization (`sasta`, `sastha`)
   - Price intent (`50k`, `rupees`)
   - Accessory intent (`cover`, `charger`)
   - Freshness (`latest`)

3. **Business signals**
   - Product rating
   - Units sold
   - Stock availability

4. **Price fitness**
   - Boosts affordable products for Tier-2/3 users

This ensures affordable, relevant, and available products rank higher.

---

## APIs Implemented

### 1. Store Product
`POST /api/v1/product`

### 2. Update Product Metadata
`PUT /api/v1/product/meta-data`

### 3. Search Products
`GET /api/v1/search/product?query=...`

All APIs are documented via Swagger.

---

## How to Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
