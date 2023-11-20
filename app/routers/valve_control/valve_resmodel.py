from pydantic import BaseModel


class valve_ops(BaseModel):
    device_id: str
    valve_status: str


class valve_status(BaseModel):
    device_id: str
    valve_status: str
    tag: str
    custom_tag: str


class ops_limit(BaseModel):
    limit: int


class custom_tag(BaseModel):
    device_id: str
    custom_tag: str


class flow_limit(BaseModel):
    limit: int
    detail: str
