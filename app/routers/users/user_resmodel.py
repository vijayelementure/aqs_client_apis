from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class activity_info(BaseModel):
    updated_by: str
    updated_at: datetime


class meta_info(BaseModel):
    ver: str
    created_by: str
    created_at: datetime
    activity: Optional[activity_info]


class dwell_info(BaseModel):
    community_id: str
    community_name: str
    dwell_id: str
    block: str
    floor_no: str
    flat_no: str
    role: str
    user_status: str


class user_status(BaseModel):
    detail: str
    message: str
    name: Optional[str]


class user_model(BaseModel):
    user_id: str
    name: str
    mobile: str
    email: str
    birth_date: str
    dp_url: str
    dwell_info: List[dwell_info]
    meta: meta_info


class general_response(BaseModel):
    detail: str
    status: str
    meta: meta_info
