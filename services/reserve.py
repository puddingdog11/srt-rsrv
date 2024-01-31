import time

from SRT import SRT, SRTLoginError
from SRT.srt import SRTTrain
from SRT.passenger import Passenger
from SRT.reservation import SRTReservation

from models.user import SrtUserModel, TrainUser
from models.ticket import Ticket

class ReserveService:

    def __init__(self, ticket : Ticket, service):
        self.ticket = ticket
        self.train_service = service
        
    def login(self):
        return self.train_service.login()
    
    def reserve(self):
        return self.train_service.reserve(self.ticket)
    
    def reserve_loop(self):
        while True:
            time.sleep(1)
            if self.reserve():
                break
            else:
                continue
        return True
        

# class ReserveService:
    
#     self.srt_user = None
#     self.srt_instance = None
#     self.reservation = None
    
#     def __init__ (self, srt_user : SrtUserModel = None, srt_instance : SRT = None):
#         if SrtUserModel is None:
#             raise Exception("SrtUserModel is not defined")
#         self.srt_user = srt_user
#         self.srt_instance = srt_instance
    
#     def login(self) -> bool:
#         try:
#             self.srt_instance.login()
#         except SRTLoginError as e:
#             return False
    
#     def search(self, ticket: Ticket) -> list[SRTTrain]:
#         trains = self.srt_instance.search_train(
#             dep=ticket.departure_station,
#             arr=ticket.destination_station,
#             date=ticket.date,
#             time=ticket.departure_time_from,
#             time_limit=ticket.departure_time_to
#         )
        
#         trains_ = []
#         for i, v  in enumerate(trains):
#             if v.dep_time <= time_limit:
#                 trains_.append(trains[i])
#             else:
#                 pass
#         return trains_
    
#     def reserve(self, passengers: List[Passenger], trains: List[SRTTrain]) -> bool:
#         is_resv = None
#         for train in trains:
#             self.srt_instance.reserve(train, passengers=passengers)
#             print("예약하였습니다")
#             self.reservation = self.srt_instance.get_reservations()
#         return is_resv is not None
    
#     def get_reservation() -> list[SRTReservation]:
#         return self.reservation