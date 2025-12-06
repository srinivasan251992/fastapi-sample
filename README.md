# FastAPI Sample

Small FastAPI project used as a Python refresher.

## Tech stack

- Python 3.11+
- FastAPI
- Uvicorn

## Run with Docker

docker build -t fastapi-sample .
docker run -p 8000:8000 fastapi-sample

## Running locally
pip install -r requirements.txt
uvicorn main:app --reload
