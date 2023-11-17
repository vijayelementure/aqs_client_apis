from fastapi import FastAPI
from app.routers import api

description = "user client interface"

app = FastAPI(
    title="Aquesa User APIs",
    summary="Provides Consumption,valve_Control,Activity_Logs & User APIs",
    description=description,
    version="1.0.0",
)


app.include_router(
    api.router,
    prefix="/api/v1",
)