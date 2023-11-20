from pydantic import BaseModel
from typing import List, Optional


class member_info(BaseModel):
    user_id: Optional[str]
    full_name: Optional[str]
    role: Optional[str]
    status: Optional[str]


class members_list(BaseModel):
    members: List[member_info]


class roles_list(BaseModel):
    roles_list: List[str]
