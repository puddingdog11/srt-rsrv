from services.config_service import YamlConfigService


# 예약 요청 가져오기

config_service = YamlConfigService('reservations.yaml')
tickets = config_service.load_reservations()

# 예약 정보로 예약 실행

# 예약 내역 리턴

# 예약 내역 알림

# 프로그램 종료