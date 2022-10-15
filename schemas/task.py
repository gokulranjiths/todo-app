from pydantic import BaseModel
from typing import List

class Task():
    id: str
    text: str
    status: str
    created_by: str

    class Config:
        orm_mode = True