from pydantic import BaseModel
from datetime import datetime

class read_model(BaseModel):
    full_name: str
    date_of_birth: datetime
    email: str