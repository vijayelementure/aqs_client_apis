from fastapi import APIRouter
from fastapi import status
from app.routers.users.members import mem_reqmodel, mem_resmodel
import datetime

router = APIRouter()


# POST api/v1/members/{dwelling_id}/ - add a members
@router.post(
    "/{dwelling_id}",
    status_code=status.HTTP_201_CREATED,
)
async def add_member(
    dwelling_id: str,req:mem_reqmodel.add_mem
):
    # buisness logic

    return {
        "message":"members added successfully"
        }
    
    

# GET api/v1/members/{dwelling_id}/ - list of members
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= mem_resmodel.members_list
)
async def read_members(
    dwelling_id: str,
):
    # buisness logic

    return list(dict)



# PATCH api/v1/members/{dwelling_id}/ - update member status
@router.patch(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
)
async def update_memstatus(
    dwelling_id: str,
):
    # buisness logic

    return {
        "message": "member status updated successfully"
    }
    
    


# DELETE api/v1/members/{dwelling_id}/ - delete members
@router.delete(
    "/{dwelling_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_member(
    dwelling_id: str,
):
    # buisness logic

    return {
        "message": "member deleted successfully"
    }
    
    
    
