from pydantic import BaseModel


class activity_logs(BaseModel):
    dwelling_id: str
