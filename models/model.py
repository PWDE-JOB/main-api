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


class jobCreation(BaseModel):
    title: str
    description: str
    skill_1: str
    skill_2: str
    skill_3: str
    skill_4: str
    skill_5: str
    pwd_friendly: bool
    
class updateJob(BaseModel):
    title: str
    description: str
    skill_1: str
    skill_2: str
    skill_3: str
    skill_4: str
    skill_5: str
    pwd_friendly: bool