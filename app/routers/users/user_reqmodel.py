from pydantic import BaseModel
from typing import Optional, List


class dwell_info(BaseModel):
    dwelling_id: Optional[str]
    user_status: Optional[str]


class patch_req(BaseModel):
    name: str
    date_of_birth: Optional[str] = "YYYY-MM-DD"
    mobile: Optional[str]
    email: str
    dwellInfo: List[str]


class logout_req(BaseModel):
    token: str
    fcm_token: str
    devid: str
