from fastapi import APIRouter, status, HTTPException
from app.routers.users.members import mem_reqmodel, mem_resmodel
from app.routers.users import user_resmodel
from app.auth import verify
from fastapi import Depends

from typing import List


router = APIRouter(
    dependencies=[Depends(verify.get_user_token)],
)


# POST api/v1/members/{dwelling_id}/ - add a user
@router.post(
    "/member",
    status_code=status.HTTP_201_CREATED,
    response_model=user_resmodel.general_response,
)
async def add_member(
    req: mem_reqmodel.add_user,
    dwelling_id: str,
):
    try:
        # buisness logic

        return {"message": "user added successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# GET api/v1/members/{dwelling_id}/ - list of members
@router.get(
    "/member",
    status_code=status.HTTP_200_OK,
    response_model=List[mem_resmodel.member_info],
)
async def get_users_list(
    dwelling_id: str,
):
    try:
        # buisness logic

        return list(dict)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# PATCH api/v1/members/{dwelling_id}/ - update member status
@router.patch(
    "/member",
    status_code=status.HTTP_200_OK,
    response_model=mem_resmodel.member_info,
)
async def update_memstatus(
    req: mem_reqmodel.update_mem,
):
    try:
        # buisness logic

        return {"message": "member status updated successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )


# DELETE api/v1/members/{user_id}/ - delete members
# @router.delete(
#     "/{user_id}",
#     status_code=status.HTTP_204_NO_CONTENT,
# )
# async def delete_member(
#     dwelling_id: str,
# ):
#     try:
#         # buisness logic

#         return None
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_204_NO_CONTENT,
#             detail=str(e),
#         )


# GET api/v1/members/{dwelling_id}/ - list of roles
@router.get(
    "/member/role",
    status_code=status.HTTP_200_OK,
    response_model=mem_resmodel.roles_list,
)
async def list_roles():
    try:
        # buisness logic

        return list(dict)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
