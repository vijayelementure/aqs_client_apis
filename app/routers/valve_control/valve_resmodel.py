from pydantic import BaseModel


class valve_ops(BaseModel):
    device_id: str
    valve_status: str


class valve_status(BaseModel):
    device_id: str
    status: str


class ops_limit(BaseModel):
    limit: int


class custom_tag(BaseModel):
    dwelling_id: str
    device_id: str
    custom_tag: str
