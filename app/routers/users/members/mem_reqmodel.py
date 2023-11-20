from pydantic import BaseModel


class add_user(BaseModel):
    dwelling_id: str
    full_name: str
    mobile: str
    email: str
    role: str


class update_mem(BaseModel):
    dwelling_id: str
    user_id: str
    status: str
