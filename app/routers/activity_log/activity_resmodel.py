from pydantic import BaseModel
from datetime import datetime


class activity_logs(BaseModel):
    dwelling_id: str
    title: str
    body: str
    timesatmp: datetime
    activty_type: str
    action_by: str
