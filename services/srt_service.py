
from SRT import SRT, SRTLoginError
from SRT.srt import SRTTrain
from SRT.passenger import Adult, Child, Disability1To3, Disability4To6, Senior

from typing import List
from models.user import TrainUser
from models.ticket import Ticket
from models.passenger import PassengerInfo, PassengerType


class SRTService:
    """SRT Service."""

    def __init__(self, user : TrainUser):
        self.user = user
        self.srt = None
        
    def login(self):
        """Login to SRT."""
        try:
            self.srt = SRT(self.user.get_id(), self.user.get_pw())
            print("Login Success!")
        except SRTLoginError as e:
            print("Login Failed.")
            print(e)
    
    def reserve(self, ticket : Ticket) -> bool:
        """Reserve tickets."""
        print("Searching Train...")
        trains = self.search_train(ticket)
        _ticket = ticket
        passengers = [self.ToPassenger(p) for p in _ticket.passengers]
        if trains is not None:
            for train in trains:
                self.reservation = self.srt.reserve(train, passengers)
                print("Reservation Success! Ticket Info: ", _ticket)
                if self.reservation:
                    return True
        print("Reservation Failed.")
        return False
    
    def search_train(self, ticket : Ticket) -> List[SRTTrain]:
        """Search train."""
        trains = self.srt.search_train(
            dep=ticket.departure_station, 
            arr=ticket.destination_station, 
            date=ticket.date, 
            time=ticket.departure_time_from,
            time_limit=ticket.departure_time_to,
            available_only=True)
        
        if len(trains) == 0:
            print("No available train.")
        
        return trains
    
    def ToPassenger(self, passenger_info : PassengerInfo):
        _type = passenger_info.passenger_type
        if _type == PassengerType.ADULT:
            return Adult()
        elif _type == PassengerType.CHILD:
            return Child()
        elif _type == PassengerType.SENIOR:
            return Senior()
        elif _type == PassengerType.DISABLED_1_3:
            return Disability1To3
        elif _type == PassengerType.DISABLED_4_6:
            return Disability4To6()
        