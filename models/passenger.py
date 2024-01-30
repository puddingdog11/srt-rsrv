from enum import Enum

from pydantic import BaseModel

# SRTrain에서 예약하기 위해 사용할 승객 클래스
class Passenger:
    def __init__(self, name, phone, type):
        self.train = None
        self.seat = None
        self.type = PassengerType(type)     

    def __str__(self):
        return f"이름: {self.name}, 전화번호: {self.phone}, 승객 유형: {self.type}"


class PassengerType(Enum):
    """
    "1": "어른/청소년",
    "2": "장애 1~3급",
    "3": "장애 4~6급",
    "4": "경로",
    "5": "어린이"
    """
    ADULT = 1
    DISABLED_1_3 = 2
    DISABLED_4_6 = 3
    ELDERLY = 4
    CHILD = 5
    
class SeatType(Enum):
    SPECIAL = 1
    GENERAL = 2
    
class PassengerInfo(BaseModel):
    seat_type : SeatType
    passenger_type: PassengerType
