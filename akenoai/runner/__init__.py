import logging
import os

import uvicorn
from fastapi import Depends, HTTPException

from akenoai import AkenoXToJs as _ran_dev

app = _ran_dev.get_app()

logger = logging.getLogger(__name__)
LOGS = logging.getLogger("[akenox]")
logger.setLevel(logging.DEBUG)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/api/openai/gpt-old")
async def get_openai(query: str):
    return await _ran_dev.randydev(
        "ai/openai/gpt-old",
        custom_dev_fast=True,
        query=query
    )

def run_fast(host: str = '0.0.0.0', port: int = 8000) -> None:
    LOGS.info(f"Running on port {port}")
    uvicorn.run(app, host=host, port=port)
    LOGS.info(f"Closing port {port}")
