from multiprocessing import Process, freeze_support

from services.config_service import YamlConfigService
from services.reserve import ReserveService
from services.srt_service import SRTService

class ReserveApplication:
    
    def __init__(self, reserve_service: ReserveService):
        self.reserve_service = reserve_service

    def run(self):
        self.reserve_service.login()
        self.reserve_service.reserve_loop()
        ...

def run_reserve(reserve_service: ReserveService):
    app = ReserveApplication(reserve_service)
    app.run()


if __name__ == '__main__':
    
    freeze_support()
    
    config_service = YamlConfigService('reservations.yaml')
    train_service = SRTService(config_service.load_user())

    processes = []

    for rsrv in config_service.load_reservations():
        process = Process(target=run_reserve, 
                                        args=(ReserveService(
                                            ticket= rsrv, 
                                            service=train_service),))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes are finished.")
