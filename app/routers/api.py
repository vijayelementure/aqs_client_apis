from fastapi import APIRouter
from app.routers.users import user_endpoint
from app.routers.consumption import csm_endpoint
from app.routers.users.members import mem_endpoint
from app.routers.valve_control import valve_endpoint
from app.routers.activity_log import activity_endpoint


router = APIRouter()

router.include_router(
    user_endpoint.router,
    prefix="/users",
    tags=["Users APIs"],
)


router.include_router(
    mem_endpoint.router,
    prefix="",
    tags=["Users APIs"],
)

router.include_router(
    csm_endpoint.router,
    prefix="/consumption",
    tags=["Consumption APIs"],
)

router.include_router(
    valve_endpoint.router,
    prefix="/valve",
    tags=["Valve Control APIs"],
)

router.include_router(
    activity_endpoint.router,
    prefix="/activity",
    tags=["Activity Log APIs"],
)
