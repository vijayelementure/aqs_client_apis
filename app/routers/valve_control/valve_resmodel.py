from pydantic import BaseModel


class valve_ops(BaseModel):
    dwelling_id: str
    device_id: str
    valve_status: bool


class valve_status(BaseModel):
    dwelling_id: str
    device_id: str
    status: bool


class ops_limit(BaseModel):
    dwelling_id: str
    limit: int


class custom_tag(BaseModel):
    dwelling_id: str
    device_id: str
    custom_tag: str
