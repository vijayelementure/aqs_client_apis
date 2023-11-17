from pydantic import BaseModel
from typing import List


class hourly_csm(BaseModel):
    hourordate: str
    consumption: int


class total_csm(BaseModel):
    dwelling_id: str
    total_consumption: int
    consumption: List[hourly_csm]
    # monthly_consumption: List[dict]


class ninty_days_csm(BaseModel):
    dwelling_id: str
    total_csm_ninty: List[dict]
