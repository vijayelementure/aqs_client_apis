from fastapi import APIRouter, status, HTTPException
from datetime import datetime
from app.routers.activity_log import activity_resmodel
from typing import List

router = APIRouter()


# GET api/v1/activity/{dwelling_id} - activity logs
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model=List[activity_resmodel.activity_logs],
)
async def activity_logs(
    dwelling_id: str,
):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "title": "string",
            "body": "string",
            "timesatmp": datetime.datetime.now(),
            "activty_type": "string",
            "action_by": "string"
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
