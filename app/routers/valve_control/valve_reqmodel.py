from pydantic import BaseModel


class custom_tag(BaseModel):
    device_id: str
    custom_tag: str


class flow_limit(BaseModel):
    limit: int


class valve_ops(BaseModel):
    device_id: str
    value: str
