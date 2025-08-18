from fastapi import FastAPI
from app.api.routes import router as api_router
from app.db.database import create_db_and_tables

app = FastAPI(title="FastAPI Backend with SQLModel")

# FastAPI automatically triggers the "startup" event when the app starts.
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(api_router)