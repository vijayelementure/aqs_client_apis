from fastapi import APIRouter,status,HTTPException
from app.routers.valve_control import valve_resmodel

router = APIRouter()


# GET api/v1/valve/{dwelling_id}/{device_id} - valve status
@router.get(
    "/{dwelling_id}/{device_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.valve_status
)
async def valve_status(dwelling_id: str,device_id: str):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "device_id": "string",
            "status": 0
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    
    

# PUT api/v1/valve/{dwelling_id}/{device_id}/- valve open/close
@router.put(
    "/{dwelling_id}/{device_id}/",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.valve_ops
)
async def valve_opcl(dwelling_id: str,device_id: str,):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "device_id": "string",
            "valve_status": 1
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    

# GET api/v1/limit/{dwelling_id}/- get limit
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.valve_ops
)
async def get_limit(dwelling_id: str,):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "limit": 100
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
    

# PATCH api/v1/limit/{dwelling_id}/- update limit
@router.patch(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.ops_limit
)
async def set_limit(dwelling_id: str,limit: int,):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "limit": 100
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )    
    

# PATCH api/v1/CustomTag/{dwelling_id}/{device_id} - update limit
@router.patch(
    "/{dwelling_id}/{device_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.ops_limit
)
async def custom_tag(dwelling_id: str,device_id: str):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "device_id": "string",
            "custom_tag": "kitchen"
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )