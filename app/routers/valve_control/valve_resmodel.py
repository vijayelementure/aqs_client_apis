from pydantic import BaseModel
from typing import List


class valve_activity(BaseModel):
    datetime: str
    action_by: str


class valve_ops(BaseModel):
    device_id: str
    valve_status: str
    activity: valve_activity


class valve_status(BaseModel):
    device_id: str
    valve_status: str
    tag: str
    custom_tag: str
    activity: valve_activity


class valve_status_all(BaseModel):
    devices: List[valve_status]


class ops_limit(BaseModel):
    limit: int


class custom_tag(BaseModel):
    device_id: str
    custom_tag: str


class flow_limit(BaseModel):
    limit: int
    detail: str
