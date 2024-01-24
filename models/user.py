
from pydantic import BaseModel

class User: 

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        ...
        
class SrtUserModel(BaseModel):
    id: str
    pw: constr(min_length=8, regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])')

    class Config:
        orm_mode = True