from fastapi import APIRouter, status, HTTPException, Depends
from datetime import datetime
from app.routers.activity_log import activity_resmodel, activity_reqmodel
from typing import List, Optional

from app.auth import verify

router = APIRouter(
    dependencies=[Depends(verify.get_user_token)],
)


# GET api/v1/activity/{dwelling_id} - activity logs
@router.get(
    "/dwelling/activity",
    status_code=status.HTTP_200_OK,
    response_model=List[activity_resmodel.activity_logs],
)
async def activity_logs(
    device_id: Optional[str],
    req: activity_reqmodel.activity_logs,
):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "title": "string",
            "body": "string",
            "timesatmp": datetime.datetime.now(),
            "activty_type": "string",
            "action_by": "string",
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
