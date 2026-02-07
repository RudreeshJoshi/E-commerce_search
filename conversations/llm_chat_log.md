# LLM Conversation Log – Ecommerce Search Service

This document captures the key conversations and assistance taken from an LLM (ChatGPT) during the development of the Ecommerce Search Service MVP.

The goal of sharing this log is to provide transparency into design decisions, trade-offs, and iterative problem-solving, as requested in the assignment guidelines.

---

## 1. Problem Understanding & Approach

**Discussion topics:**
- Understanding the search problem for an e-commerce platform targeting Tier-2 and Tier-3 cities in India
- Handling real-world search issues such as:
  - Typographical errors (e.g. "Ifone")
  - Hinglish queries (e.g. "Sasta iPhone")
  - Price-sensitive intent (e.g. "50k rupees")
  - Mixed catalog results (phones, accessories, covers)

**Outcome:**
- Decided to build a **hybrid ranking-based search service** instead of simple filtering.
- Focused on **explainability and customer-centric relevance**, not ML-heavy approaches.

---

## 2. System & Code Structure Design

**Discussion topics:**
- Microservice boundaries
- Folder structure for a production-style FastAPI service
- Separation of concerns between:
  - API layer
  - Business logic (ranking, query parsing)
  - Data storage (catalog)

**Outcome:**
- Adopted a layered architecture:
  - `app/api` → HTTP endpoints
  - `app/services` → ranking, query parsing, catalog
  - `app/models` → Pydantic schemas
- Chose an **in-memory catalog** for MVP simplicity and low latency.

---

## 3. Ranking Strategy Design

**Discussion topics:**
- How to rank thousands of matching products meaningfully
- Balancing relevance vs affordability for Indian Tier-2/3 users
- Which signals matter most in early-stage marketplaces

**Key signals implemented:**
- Text relevance (fuzzy matching)
- Query intent (cheap, latest, accessory, price cap)
- Business signals (rating, stock availability, units sold)
- Price fitness

**Outcome:**
- Implemented a **hybrid, rule-based ranking algorithm** that is:
  - Fast (<1000ms)
  - Deterministic
  - Easy to explain and debug

---

## 4. Query Intent Handling

**Discussion topics:**
- Detecting intent from short, unstructured queries
- Supporting Hinglish without heavy NLP models
- Extracting numeric price intent

**Examples handled:**
- "Sasta iPhone"
- "Ifone 16"
- "iPhone 50k rupees"
- "iPhone cover strong"

**Outcome:**
- Built a lightweight query parser:
  - Hinglish normalization
  - Regex-based price extraction
  - Keyword-based intent flags
- Passed parsed intent into the ranking layer.

---

## 5. Data Bootstrapping Strategy

**Discussion topics:**
- Scraping vs synthetic data
- Ethical and practical constraints of scraping e-commerce data
- Simulating real marketplace signals

**Outcome:**
- Scraped product titles/descriptions for realism
- Generated synthetic business metrics (sales, ratings, stock)
- Documented this clearly in the README

---

## 6. API Design & Validation

**Discussion topics:**
- Designing APIs aligned with the problem statement
- Ensuring graceful error handling
- Keeping APIs simple and testable

**APIs implemented:**
- Store product
- Update product metadata
- Search products
- Health check

**Outcome:**
- APIs exposed via Swagger UI for easy manual testing
- Clear request/response contracts using Pydantic models

---

## 7. Testing Strategy (MVP Scope)

**Discussion topics:**
- What level of testing is sufficient for an MVP
- Avoiding overengineering
- Ensuring core flows work

**Outcome:**
- Added basic tests using FastAPI TestClient:
  - Product creation
  - Metadata updates
  - Search ranking behavior
- Focused on behavior validation rather than full coverage.

---

## 8. Deployment & Environment Issues

**Discussion topics:**
- Running FastAPI on Windows
- Python PATH and uvicorn issues
- Dockerization for deployment
- Free-tier cloud deployment options

**Issues encountered:**
- PowerShell multiline prompt (`>>`)
- `uvicorn` not found in PATH
- Nested git repository issues
- Render root endpoint returning 404

**Outcome:**
- Resolved issues iteratively
- Used `python -m uvicorn` for reliability
- Deployed successfully on Render
- Validated service via `/docs` endpoint

---

## 9. Final MVP Validation

**Discussion topics:**
- Manual testing via Swagger UI
- Verifying ranking behavior for different query types
- Ensuring explainability of results

**Outcome:**
- Confirmed correct behavior for:
  - Typo tolerance
  - Hinglish intent
  - Price-based ranking
  - Accessory vs phone differentiation
- Finalized MVP as submission-ready.

---

## 10. Summary

The LLM was used as a **design and problem-solving assistant**, not as a code generator alone.

It helped with:
- Architecture decisions
- Ranking strategy design
- Query intent handling
- Debugging development and deployment issues
- Improving documentation and clarity

All final design decisions, code implementation, and testing were performed and validated by the developer.
