# main.py
from fastapi import FastAPI
import uvicorn
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="FastAPI Machine Learning API")
    parser.add_argument("--port", type=int, default=8000, help="Port number to bind the FastAPI application")
    return parser.parse_args()

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

if __name__ == "__main__":
    args = parse_arguments()
    uvicorn.run(app, host="127.0.0.1", port=args.port, reload=True)
