from pydantic import BaseModel
from typing import List


class total_csm(BaseModel):
    dwelling_id: str
    day_total_consumption: int
    hourly_consumption: List[dict]
    monthly_consumption: List[dict]


class ninty_days_csm(BaseModel):
    dwelling_id: str
    total_csm_ninty: List[dict]
