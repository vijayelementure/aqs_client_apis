from pydantic import BaseModel
from typing import List

class members_list(BaseModel):
    members: List[dict]
    