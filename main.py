#credits goes to this owner.
from fastapi import FastAPI, Query
from akenoai import AkenoXJs

# Initialize the AkenoXJs instance
js = AkenoXJs()

# Create the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# New route for xnxx search
@app.get("/akeno/xnxxsearch-v2")
async def xnxx_search(query: str = Query(..., description="Search query for XNXX")):
    try:
        response = await js.xnxx_search(query)  # Assuming AkenoXJs has xnxx_search function
        return {"randydev": {"results": response}}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
