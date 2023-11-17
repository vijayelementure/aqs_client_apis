from pydantic import BaseModel
from typing import List


class add_mem(BaseModel):
    full_name: str
    phone_number: str
    email: str
    role: List[str]


class update_mem(BaseModel):
    status: str
