from pydantic import BaseModel
from typing import List

class inputSignupEmployee(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    email: str
    password: str
    disability: str
    skills: List[str]
    
class inputSignupEmployer(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    email: str
    password: str

class loginCreds(BaseModel):
    email: str
    password: str