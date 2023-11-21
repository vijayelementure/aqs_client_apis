from fastapi import APIRouter, status, HTTPException, Depends
from app.routers.valve_control import valve_resmodel, valve_reqmodel
from app.auth import verify
from typing import List

router = APIRouter(
    dependencies=[Depends(verify.get_user_token)],
)


# GET api/v1/valve/{dwelling_id}/{device_id} - valve status
@router.get(
    "/dwelling/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model=List[valve_resmodel.valve_status],
)
async def valve_status():
    try:
        # buisness logic

        return {
            "device_id": "string",
            "status": "string",
            "tag": "string",
            "custom_tag": "string",
            "activity": {
                "datetime": "string",
                "action_by": "string",
            },
        }  # Noqa

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# PUT api/v1/valve/{dwelling_id}/{device_id}/- valve open/close
@router.put(
    "/dwelling/{dwelling_id}/valve",
    status_code=status.HTTP_200_OK,
    response_model=valve_resmodel.valve_ops,
)
async def valve_opcl(
    dwelling_id: str,
    req: valve_reqmodel.valve_ops,
):
    try:
        # buisness logic

        return {
            "device_id": "string",
            "valve_status": "string",
            "activity": {
                "datetime": "string",
                "action_by": "string",
            },
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# GET api/v1/limit/{dwelling_id}/- get limit
@router.get(
    "/dwelling/{dwelling_id}/limit",
    status_code=status.HTTP_200_OK,
    response_model=valve_resmodel.ops_limit,
)
async def get_limit(
    dwelling_id: str,
):
    try:
        # buisness logic

        return {"dwelling_id": "string", "limit": 100}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# PATCH api/v1/limit/{dwelling_id}/- set limit
@router.patch(
    "/dwelling/{dwelling_id}/limit",
    status_code=status.HTTP_200_OK,
    response_model=valve_resmodel.flow_limit,
)
async def set_limit(
    dwelling_id: str,
    req: valve_reqmodel.flow_limit,
):
    try:
        # buisness logic

        return {"device_id": "string", "limit": 100}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )


# PATCH api/v1/CustomTag/{dwelling_id}/{device_id} - custom_tag
@router.patch(
    "/dwelling/{dwelling_id}/valve",
    status_code=status.HTTP_200_OK,
    response_model=valve_resmodel.custom_tag,
)
async def custom_tag(
    dwelling_id: str,
    req: valve_reqmodel.custom_tag,
):
    try:
        # buisness logic

        return {
            "device_id": "string",
            "custom_tag": "kitchen",
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )
