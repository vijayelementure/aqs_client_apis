from pydantic import BaseModel


class add_user(BaseModel):
    full_name: str
    phone_number: str
    email: str
    role: str


class update_mem(BaseModel):
    status: str
