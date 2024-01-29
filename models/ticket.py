from pydantic import BaseModel
from enum import Enum
from passenger import PassengerInfo

class Ticket(BaseModel):
    passengers: List[PassengerInfo]
    departure_station: str
    destination_station: str
    date: str
    departure_time_from: str
    departure_time_to: str

    def display_info(self):
        print("Reservation Information:")
        print("Passenger Type:", self.passenger_type)
        print("Passenger Count:", self.passenger_count)
        print("Departure Station:", self.departure_station)
        print("Destination Station:", self.destination_station)
        print("Departure Time:", self.departure_time_from)
        print("Departure Time Range:", self.departure_time_to)


