from pydantic import BaseModel
from typing import Optional


class activity_logs(BaseModel):
    dwelling_id: str
    device_id: Optional[str]
