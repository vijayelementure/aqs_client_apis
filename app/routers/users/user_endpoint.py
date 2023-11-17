from fastapi import APIRouter
from fastapi import status
from app.routers.users import user_resmodel
from app.routers.users import user_reqmodel
import datetime

router = APIRouter()


# GET /api/v1/user_section/{phone_number}/ - Get a status of user
@router.get(
    "/{phone_number}",
    status_code=status.HTTP_200_OK,
)
async def read_status(
    phone_number: str,
):
    # buisness logic

    return {
        "message":"Signed in Successfully"
        }



# GET /api/v1/user_section/{dwelling_id}/ - Get user
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= user_resmodel.read_model
)
async def read_one(
    dwelling_id: str,
):
    # buisness logic

    return {
        "full_name": "string",
        "date_of_birth": datetime,
        "email": "string"
        }



# PATCH /api/v1/user_section/{phone_number}/ - patch user
@router.patch(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
)
async def update_user(
    dwelling_id: str, req:user_reqmodel.patch_req
):
    # buisness logic

    return {
        "message": "signup successful",
        }
    


# PATCH /api/v1/user_section/{user_name}/ - patch user_name
@router.patch(
    "/{user_name}",
    status_code=status.HTTP_200_OK,
)
async def update_name(
    user_name: str,
):
    # buisness logic

    return {
        "message": "name changed",
        }
    
    

# PATCH /api/v1/user_section/{dwelling_id} - logout 
@router.get(
    "/{dwelling_id}/",
    status_code=status.HTTP_200_OK,
)
async def log_out(
    dwelling_id: str,req: user_reqmodel.logout_req
):
    # buisness logic

    return {
        "message": "logout successfully",
        }
    

