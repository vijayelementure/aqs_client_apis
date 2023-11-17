from fastapi import APIRouter, HTTPException, status
from app.routers.users import user_resmodel
from app.routers.users import user_reqmodel
import datetime


router = APIRouter()


# GET /api/v1/user_section/{phone_number}/ - Get a status of user # verify user
@router.get(
    "/{phone_number}",
    status_code=status.HTTP_200_OK,
    response_model=user_resmodel.user_status,
)
async def read_status(
    phone_number: str,
):
    try:
        # buisness logic here
        return {"message": "Signed in Successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# GET /api/v1/user_section/{dwelling_id}/ - Get user
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model=user_resmodel.read_model,
)
async def read_one(
    dwelling_id: str,
):
    try:
        # buisness logic

        return {
            "full_name": "string",
            "date_of_birth": datetime,
            "email": "string",
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# PATCH /api/v1/user_section/{phone_number}/ - patch user
@router.patch(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model=user_resmodel.general_response,
)
async def update_user(dwelling_id: str, req: user_reqmodel.patch_req):
    try:
        # buisness logic

        return {
                "message": "signup successful",  # response as get user
                }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )


# PATCH /api/v1/user_section/{user_name}/ - patch user_name # no need
@router.patch(
    "/{user_name}",
    status_code=status.HTTP_200_OK,
    response_model=user_resmodel.general_response,
)
async def update_name(
    user_name: str,
):
    try:
        # buisness logic

        return {
            "message": "name changed",
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )


# PATCH /api/v1/user_section/{dwelling_id} - logout
@router.post(
    "/{dwelling_id}/",
    status_code=status.HTTP_200_OK,
    response_model=user_resmodel.general_response,
)
async def log_out(dwelling_id: str, req: user_reqmodel.logout_req):
    try:
        # buisness logic

        return {
            "message": "logout successfully",
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )
