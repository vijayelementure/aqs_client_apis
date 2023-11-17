from pydantic import BaseModel
from datetime import datetime


class patch_req(BaseModel):
    full_name: str
    date_of_birth: datetime
    email: str


class logout_req(BaseModel):
    token: str
    fcm_token: str
    devid: str
