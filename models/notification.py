from pydantic import BaseModel

class NotificationModel(BaseModel):
    ...

class Aligo(NotificationModel):
    key: str
    user_id: str
    sender: str
    receiver: str    
    
    