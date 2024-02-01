from multiprocessing import Process, freeze_support

from services.config_service import YamlConfigService
from services.reserve import ReserveService
from services.srt_service import SRTService
from services.notification import NotificationService, AligoNotificationService

from models.notification import Aligo


class ReserveApplication:
    
    def __init__(self, 
                 reserve_service: ReserveService,
                 notification_service: NotificationService):
        self.reserve_service = reserve_service
        self.notification_service = notification_service

    def run(self):
        self.reserve_service.login()
        reserve_result = self.reserve_service.reserve_loop()
        if reserve_result:
            print("Reservation Success!")
            self.notification_service.send(
                f"예약이 완료되었습니다!\nTicket Info: {self.reserve_service.get_reservation()}")
        else:
            print("Reservation Failed.")

def run_reserve(
    reserve_service: ReserveService,
    notification_service: NotificationService):
    app = ReserveApplication(
        reserve_service,
        notification_service)
    app.run()


if __name__ == '__main__':
    
    freeze_support()
    
    config_service = YamlConfigService('reservations.yaml')
    train_service = SRTService(config_service.load_user())
    AligoModel = Aligo(**config_service.load_notification()["aligo"])
    notification_service = AligoNotificationService(AligoModel)

    processes = []

    for rsrv in config_service.load_reservations():
        process = Process(target=run_reserve, 
                                        args=(ReserveService(
                                            ticket= rsrv, 
                                            service=train_service),
                                              notification_service,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes are finished.")
