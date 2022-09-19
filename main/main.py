from fastapi import FastAPI, Request 
from main.routers import router

app = FastAPI(
    title="BaseApp",
    description="",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)
app.include_router(router)