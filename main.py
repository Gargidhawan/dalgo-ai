# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

# You can add more endpoints here as needed
