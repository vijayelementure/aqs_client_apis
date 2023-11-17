from fastapi import APIRouter,status,HTTPException
from app.routers.consumption import csm_resmodel

router = APIRouter()


# GET api/v1/csm/{dwelling_id}/ - total consumption
@router.get(
    "/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= csm_resmodel.total_csm
)
async def total_csm(dwelling_id: str,year: int, month: int, date: int):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "day_total_consumption": 7878,
            "hourly_consumption":[{"01":12},
                                {"02":34},
                                {"03":32},
                                {"04":56},
                                {"05":12},],
            "monthly_consumption": [{"01":567},
                                    {"02":678},
                                    {"03":876},
                                    {"04":890},
                                    {"16":678},]
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
    

# GET api/v1/csm/last_ninty/{dwelling_id}/ - total ninty consumption
@router.get(
    "/last_ninty_days/{dwelling_id}",
    status_code=status.HTTP_200_OK,
    response_model= csm_resmodel.ninty_days_csm
)
async def last_ninty_csm(dwelling_id: str,year: int, month: int, date: int):
    try:
        # buisness logic

        return {
            "dwelling_id": "string",
            "total_csm_ninty": [{"16-09-2023":200},
                                {"17-09-2023":400},
                                {"18-10-2023":600},
                                {"19-10-2023":800},
                                {"16-11-2023":200},
                                {"20-11-2023":200},]
            }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )