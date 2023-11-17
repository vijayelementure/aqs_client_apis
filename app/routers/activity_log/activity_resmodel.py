from pydantic import BaseModel
from datetime import datetime
from typing import List


class activity_logs(BaseModel):
    dwelling_id: str
    title: str
    body: str
    timesatmp: datetime
    activty_type: List[str]
