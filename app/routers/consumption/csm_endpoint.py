from fastapi import APIRouter, status, Depends
from app.routers.consumption import csm_resmodel
from app.auth import verify

router = APIRouter(
    dependencies=[Depends(verify.get_user_token)],
)


@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model=csm_resmodel.total_csm,
)
async def consumption(dwelling_id: str, start_date: str, end_date: str):
    return {"message": "get consumption"}
