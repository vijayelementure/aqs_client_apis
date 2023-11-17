from fastapi import APIRouter
from fastapi import status
from app.routers.valve_control import valve_resmodel

router = APIRouter()


# GET api/v1/valve/{dwelling_id}/{device_id} - valve status
@router.get(
    "/{dwelling_id}/{device_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.valve_status
)
async def valve_status(
    dwelling_id: str,device_id: str
):
    # buisness logic

    return {
        "dwelling_id": "string",
        "device_id": "string",
        "status": 0
        }
    
    

# PUT api/v1/valve/{dwelling_id}/{device_id}/- valve open/close
@router.put(
    "/{dwelling_id}/{device_id}/",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.valve_ops
)
async def valve_opcl(
    dwelling_id: str,device_id: str,
):
    # buisness logic

    return {
        "dwelling_id": "string",
        "device_id": "string",
        "valve_status": 1
        }
    
    

# GET api/v1/limit/{dwelling_id}/- get limit
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.valve_ops
)
async def get_limit(
    dwelling_id: str,
):
    # buisness logic

    return {
        "dwelling_id": "string",
        "limit": 100
        }
    
    

# PATCH api/v1/limit/{dwelling_id}/- update limit
@router.patch(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.ops_limit
)
async def set_limit(
    dwelling_id: str,limit: int,
):
    # buisness logic

    return {
        "dwelling_id": "string",
        "limit": 100
        }
    
    

# PATCH api/v1/CustomTag/{dwelling_id}/{device_id} - update limit
@router.patch(
    "/{dwelling_id}/{device_id}",
    status_code=status.HTTP_200_OK,
    response_model= valve_resmodel.ops_limit
)
async def custom_tag(
    dwelling_id: str,device_id: str
):
    # buisness logic

    return {
        "dwelling_id": "string",
        "device_id": "string",
        "custom_tag": "kitchen"
        }