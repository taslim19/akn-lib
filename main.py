# main.py

from fastapi import FastAPI
from akenoai import AkenoXJs

# Initialize the AkenoXJs instance
js = AkenoXJs()

# Create the FastAPI app
app = FastAPI()

# You may need to add routes or other configurations here
# For example, if there are specific routes provided by the library:
# app.include_router(js.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
