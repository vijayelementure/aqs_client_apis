from fastapi import APIRouter, status, HTTPException
from app.routers.users.members import mem_reqmodel, mem_resmodel


router = APIRouter()


# POST api/v1/members/{dwelling_id}/ - add a members
@router.post(
    "/{dwelling_id}",
    status_code=status.HTTP_201_CREATED,
)
async def add_member(dwelling_id: str, req: mem_reqmodel.add_mem):
    try:
        # buisness logic

        return {
                "message": "members added successfully"
                }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# GET api/v1/members/{dwelling_id}/ - list of members
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model=mem_resmodel.members_list
)
async def read_members(dwelling_id: str,):
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
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
)
async def update_memstatus(dwelling_id: str,):
    try:
        # buisness logic

        return {
                "message": "member status updated successfully"
                }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )


# DELETE api/v1/members/{dwelling_id}/ - delete members
@router.delete(
    "/{dwelling_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_member(dwelling_id: str,):
    try:
        # buisness logic

        return {
                "message": "member deleted successfully"
               }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=str(e),
        )
