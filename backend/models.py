from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str
    course: str
    email: str
    gender: str
    id: Optional[str] = None