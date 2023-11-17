from pydantic import BaseModel
from typing import Optional


class patch_req(BaseModel):
    full_name: str
    date_of_birth: Optional[str] = "YYYY-MM-DD"
    email: str


class logout_req(BaseModel):
    token: str
    fcm_token: str
    devid: str
