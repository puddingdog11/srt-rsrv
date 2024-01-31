
from SRT import SRT, SRTLoginError
from SRT.srt import SRTTrain
from SRT.passenger import Adult, Child, Disability1To3, Disability4To6, Senior

from typing import List
from models.user import TrainUser
from models.ticket import Ticket


class SRTService:
    """SRT Service."""

    def __init__(self, user : TrainUser):
        self.user = user
        
    def login(self) -> bool:
        """Login to SRT."""
        try:
            self.srt = SRT(self.user.get_id(), self.user.get_pw())
            print("Login Success!")
        except SRTLoginError as e:
            print("Login Failed.")
            print(e)
            return False
        return True
    
    def reserve(self, ticket : Ticket) -> bool:
        """Reserve tickets."""
        print("Searching Train...")
        trains = self.search_train(ticket)
        if trains is not None:
            for train in trains:
                self.reservation = self.srt.reserve(train, self.ticket)
                print("Reservation Success! Ticket Info: ", self.ticket)
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