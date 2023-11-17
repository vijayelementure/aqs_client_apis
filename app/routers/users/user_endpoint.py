from fastapi import APIRouter, HTTPException, status
from app.routers.users import user_resmodel
from app.routers.users import user_reqmodel


router = APIRouter()


# GET /api/v1/verify_user/{phone_number}/ -verify user
@router.get(
    "/verify_user/{phone_number}",
    status_code=status.HTTP_200_OK,
    response_model=user_resmodel.user_model,
)
async def verify_user(
    phone_number: str,
):
    try:
        # buisness logic here
        return {
                    "user_id": "string",
                    "name": "string",
                    "mobile": "string",
                    "email": "string",
                    "birth_date": "string",
                    "dp_url": "string",
                    "dwell_info": [
                        {
                            "community_id": "string",
                            "community_name": "string",
                            "dwell_id": "string",
                            "block": "string",
                            "floor_no": "string",
                            "flat_no": "string",
                            "role": "string",
                            "user_status": "string"
                        }
                    ],
                    "meta": {
                        "ver": "string",
                        "created_by": "string",
                        "created_at": "2023-11-17T12:04:55.672Z",
                        "activity": {
                                    "updated_by": "string",
                                    "updated_at": "2023-11-17T12:04:55.672Z"
                                     }
                    }
                    }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# GET /api/v1/get_user/{user_id}/ - Get user
@router.get(
    "/get_user/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=user_resmodel.user_model,
)
async def get_user():
    try:
        # buisness logic

        return {
                    "user_id": "string",
                    "name": "string",
                    "mobile": "string",
                    "email": "string",
                    "birth_date": "string",
                    "dp_url": "string",
                    "dwell_info": [
                        {
                            "community_id": "string",
                            "community_name": "string",
                            "dwell_id": "string",
                            "block": "string",
                            "floor_no": "string",
                            "flat_no": "string",
                            "role": "string",
                            "user_status": "string"
                        }
                    ],
                    "meta": {
                        "ver": "string",
                        "created_by": "string",
                        "created_at": "2023-11-17T12:04:55.672Z",
                        "activity": {
                                    "updated_by": "string",
                                    "updated_at": "2023-11-17T12:04:55.672Z"
                                     }
                    }
                    }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# PATCH /api/v1/users/{user_id}/ - patch user
@router.patch(
    "/{user_id}",
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
