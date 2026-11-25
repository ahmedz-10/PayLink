
import os
import psycopg

from fastapi import FastAPI
app = FastAPI(title="PayLink API")


@app.get("/")
def home():
    return {"message": "PayLink application is running!"}


@app.get("/health")
def health():
    try:
        with psycopg.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=5432,
            dbname=os.getenv("DB_NAME", "paylink"),
            user=os.getenv("DB_USER", "paylink_user"),
            password=os.getenv("DB_PASSWORD", "paylink_password")
        ) as connection:
            connection.execute("SELECT 1")

        return {
            "application": "running",
            "database": "connected"
        }

    except Exception:
        return {
            "application": "running",
            "database": "disconnected"
        }
