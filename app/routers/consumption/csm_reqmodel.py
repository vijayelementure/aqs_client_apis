from pydantic import BaseModel

# from datetime import datetime


class consumption(BaseModel):
    dwelling_id: str
    start_date: str
    end_date: str
