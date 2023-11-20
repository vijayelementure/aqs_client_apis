from fastapi import APIRouter, status, Depends
from app.routers.consumption import csm_resmodel, csm_reqmodel
from app.auth import verify

router = APIRouter(
    dependencies=[Depends(verify.get_user_token)],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=csm_resmodel.total_csm,
)
async def consumption(req: csm_reqmodel.consumption):
    return {"message": "get consumption"}
