import sentry_sdk

from fastapi import FastAPI
from app.routers import api
from mangum import Mangum

description = "user client interface"

app = FastAPI(
    title="Aquesa Mobile APIs",
    summary="Provides Consumption,valve_Control,Activity_Logs & User APIs",
    description=description,
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

sentry_sdk.init(
    dsn="https://897d8f1129ad9ed0502fae4933bbad9b@o4506240431947776.ingest.sentry.io/4506240433258496",  # noqa
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


app.include_router(
    api.router,
    prefix="/api/v1",
)


@app.get("/")
async def root():
    return {"message": "Aquesa Mobile APIs"}


handler = Mangum(app)
