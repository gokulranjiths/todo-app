from pydantic import BaseModel
from typing import List

class Task():
    id: str
    text: str

    class Config:
        orm_mode = True