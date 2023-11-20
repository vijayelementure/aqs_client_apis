from pydantic import BaseModel, EmailStr
from typing import List, Optional


class member_info(BaseModel):
    user_id: Optional[str]
    full_name: Optional[str]
    mobile: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    status: Optional[str]


class roles_list(BaseModel):
    roles: List[str]
