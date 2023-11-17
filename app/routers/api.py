from fastapi import APIRouter
from app.routers.users import user_endpoint
from app.routers.consumption import csm_endpoint
from app.routers.users.members import mem_endpoint
from app.routers.valve_control import valve_endpoint
from app.routers.activity_log import activity_endpoint


router = APIRouter()

router.include_router(
    user_endpoint.router,
    prefix="/user_section",
    tags=["Users APIs"],
)


router.include_router(
    mem_endpoint.router,
    prefix="/members",
    tags=["Users APIs"],
)

router.include_router(
    csm_endpoint.router,
    prefix="/consumption",
    tags=["Consumption APIs"],
)

router.include_router(
    valve_endpoint.router,
    prefix="/valve_control",
    tags=["Valve Control APIs"],
)

router.include_router(
    activity_endpoint.router,
    prefix="/activity_section",
    tags=["Activity Log APIs"],
)
