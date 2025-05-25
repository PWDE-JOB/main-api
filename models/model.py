from pydantic import BaseModel
from typing import List

class inputSignup(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    email: str
    password: str
    disability: str
    skills: List[str]

class loginCreds(BaseModel):
    email: str
    password: str