from pydantic import BaseModel
from typing import Optional


class dwell_info(BaseModel):
    dwelling_id: Optional[str]
    role: Optional[str]
    user_status: Optional[str]


class patch_req(BaseModel):
    name: Optional[str]
    date_of_birth: Optional[str] = "YYYY-MM-DD"
    email: Optional[str]


class logout_req(BaseModel):
    fcm_token: str
    devid: str
