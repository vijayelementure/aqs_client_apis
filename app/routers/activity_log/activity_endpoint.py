from fastapi import APIRouter
from fastapi import status
from datetime import datetime
from typing import List
from app.routers.activity_log import activity_resmodel

router = APIRouter()


# GET api/v1/activity/{dwelling_id} - valve status
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= activity_resmodel.activity_logs
)
async def activity_logs(
    dwelling_id: str,
):
    # buisness logic

    return {
            "dwelling_id": "string",
            "title": "string",
            "body": "string",
            "timesatmp": datetime.datetime.now(),
            "activty_type": List["string"],
        }