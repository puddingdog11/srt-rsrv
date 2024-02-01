import yaml

from models.ticket import Ticket
from models.passenger import PassengerInfo, SeatType, PassengerType
from models.user import SrtUserModel

class ConfigService:
    def __init__(self, path):
        self.path = path


class YamlConfigService(ConfigService):
    
    def __init__(self, path):
        super().__init__(path)
        
    def load(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    
    def load_reservations(self) -> list[Ticket]:
        rsrv_list = self.load()['Reservations']

        reservations = []
        
        for rsrv in rsrv_list:
            passengers = []
            passenger_list = rsrv["Passengers"]
            for _type, count in passenger_list.items():
                if _type == "Adult":
                    adults = [PassengerInfo(
                        seat_type = SeatType.GENERAL,
                        passenger_type = PassengerType.ADULT
                        ) for i in range(count)]
                    passengers.extend(adults)
                elif _type == "Child":
                    children = [PassengerInfo(
                        seat_type=SeatType.GENERAL,
                        passenger_type=PassengerType.CHILD
                    ) for i in range(count)]
                    passengers.extend(children)
                elif _type == "Senior":
                    seniors = [PassengerInfo(
                        seat_type=SeatType.GENERAL,
                        passenger_type=PassengerType.ELDERLY
                    ) for i in range(count)]
                    passengers.extend(seniors)
                elif _type == "Disability1To3":
                    disability1to3 = [PassengerInfo(
                        seat_type=SeatType.GENERAL,
                        passenger_type=PassengerType.DISABLED_1_3
                    ) for i in range(count)]
                    passengers.extend(disability1to3)
                elif _type == "Disability4To6":
                    disability4to6 = [PassengerInfo(
                        seat_type=SeatType.GENERAL,
                        passenger_type=PassengerType.DISABLED_4_6
                    ) for i in range(count)]
                    passengers.extend(disability4to6)    
            
            ticket = Ticket(
                departure_station=rsrv['Ticket']['depature'],
                destination_station=rsrv['Ticket']['arrival'],
                date=rsrv['Ticket']['date'],
                departure_time_from=rsrv['Ticket']['departure_time'],
                departure_time_to=rsrv['Ticket']['time_limit'],
                passengers=passengers
            )
            
            reservations.append(ticket)
            
        return reservations
        
    def load_user(self) -> SrtUserModel:
        user = self.load()['User']
        srt_user = SrtUserModel(
            id = user['id'],
            pw = user['pw']
        )
            
        return srt_user
    
    def load_notification(self) -> dict:
        return self.load()['Notification']