from requests import Response, post

from models.notification import NotificationModel, Aligo

class NotificationService:
    def send(self, message: str) -> bool:
        pass
    
class AligoNotificationService(NotificationService):
    
    def __init__(self, aligo: Aligo):
        self.base_url = "https://apis.aligo.in/send/"
        self.aligo = aligo
    
    def send(self, message: str) -> bool:
        
        data = {
            'key': self.aligo.key,
            'user_id': self.aligo.user_id,
            'sender': self.aligo.sender,
            'receiver': self.aligo.receiver,
            'msg': message,
        }
        
        response = post(
            url = self.base_url,
            data = data
        )
        
        if response.status_code == 200:
            result = response.json()
            if result["result_code"] == "1":
                print("Message sent successfully")
                return True
            else:
                print("Failed to send message")
                return False
        else:
            print("HTTP request failed")
            return False
        