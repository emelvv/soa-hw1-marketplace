"""Minimal Catalog Service for the architecture homework."""

from fastapi import FastAPI


app = FastAPI(
    title="Catalog Service",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.get("/health", status_code=200)
def health() -> dict[str, str]:
    return {"status": "ok"}
