
from pydantic import BaseModel, Field, validator

class User: 

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        ...
 
class SrtUserModel(BaseModel):
    id: str
    pw: str
    
    @validator('pw')
    def validate_password(cls, pw):
        # 패스워드가 최소 8자 이상이고, 소문자, 대문자, 숫자, 특수 문자를 포함하는지 검사
        if len(pw) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.islower() for char in pw):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char.isupper() for char in pw):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.isdigit() for char in pw):
            raise ValueError('Password must contain at least one digit')
        if not any(char in "@#$%^&+=" for char in pw):
            raise ValueError('Password must contain at least one of @#$%^&+=')
        return pw
    
    class Config:
        orm_mode = True