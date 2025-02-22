from fastapi import FastAPI, Query
import httpx  # For making async requests

app = FastAPI()

# AkenoX API Key (Change this if needed)
API_KEY = "randigithub356"
BASE_URL = "https://akn-lib.onrender.com"

async def xnxx_search(query: str):
    """Manually fetch search results from AkenoX API."""
    url = f"{BASE_URL}/akeno/xnxxsearch-v2?query={query}"
    headers = {"x-akeno-key": API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        return {"error": f"API request failed with status {response.status_code}"}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/akeno/xnxxsearch-v2")
async def xnxx_search_endpoint(query: str = Query(..., description="Search query for XNXX")):
    try:
        results = await xnxx_search(query)
        return {"randydev": {"results": results}}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
