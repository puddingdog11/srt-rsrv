import time
import datetime
import smtplib
from email.mime.text import MIMEText

from SRT import SRT, SRTLoginError
from SRT.srt import SRTTrain

def set_user_info():
    srtid = input("srt id를 입력하세요 : \n")
    srtpw = input("srt 비밀번호를 입력하세요 : \n")

    info = {
        "id" : srtid,
        "pw" : srtpw,
    }
    return info

def set_resv_info():
    dep = input("출발지를 입력하세요 : \n ")
    arr = input("도착지를 입력하세요 : \n")
    date = input("예약 날짜를 입력하세요(ex: 20210101) : \n")
    time = input("출발 시간을 입력하세요(ex: 144000) : \n")
    time_limit = input("출발시간 한도를 입력하세요(ex: 180000) : \n")
    info = {
        "dep" : dep,
        "arr" : arr,
        "date" : date,
        "time" : time,
        "time_limit" : time_limit,
    }
    print(info)
    return info

def refine_trains(trains: SRTTrain, time_limit: str):
    trains_ = []
    for i, v  in enumerate(trains):
        if v.dep_time <= time_limit:
            trains_.append(trains[i])
        else:
            pass
    return trains_

def set_naver_user():
    user = input("네이버 아이디를 입력하세요 : \n")
    pw = input("네이버 비밀번호를 입력하세요 : \n")
    info = {
        "id" : user,
        "pw" : pw
    }
    return info

def send_naver_email(naver_user, ticket):
    s = smtplib.SMTP('smtp.naver.com', 587)

    s.starttls()

    s.login(
        user = naver_user["id"],
        password = naver_user["pw"]
    )

    msg = MIMEText(f"열차가 예약되었습니다. \n20분 내로 결제해주세요. \n티켓정보: {ticket}" )
    msg["Subject"] = "열차 예약 완료"
    msg["From"] = f"{naver_user['id']}@naver.com"
    msg["To"] = f"{naver_user['id']}@naver.com"
    print("메일 전송 중..")
    try:
        s.sendmail(f"{naver_user['id']}@naver.com", f"{naver_user['id']}@naver.com", msg.as_string())
        print('메일 전송 완료!')
    except Exception as e:
        print("메일 전송 실패..")
        print(e)
    finally:
        s.quit()

def main():
    
    srt = None
    while not srt:
        try :
            user = set_user_info()
            srt = SRT(srt_id=user["id"], srt_pw=user["pw"])
            print("로그인 하였습니다")
        except SRTLoginError as e:
            print(e)

    if input("결과를 메일로 전송하시겠습니까? (y/n) ") == "Y" or "y":
        is_send_naver_email = True
        naver_user = set_naver_user()

    resv = set_resv_info()
    trains_refined = None
    while not trains_refined:
        trains = srt.search_train(resv["dep"], resv["arr"], resv["date"], resv["time"])
        trains_refined = refine_trains(trains=trains, time_limit=resv["time_limit"])
        if trains_refined:
            print("예약 가능한 열차 : ", trains_refined)
        else : 
            print(f"{datetime.datetime.now()} - 예약 가능한 열차가 없습니다. 다시 시도합니다.")
        time.sleep(1)
        
    is_resv = None
    while not is_resv:
        for i in trains_refined:
            if not is_resv:
                # todo: 예약시 알람 보내기
                srt.reserve(i)
                print("예약하였습니다")
                is_resv = srt.get_reservations()
                if is_send_naver_email:
                    send_naver_email(naver_user=naver_user, ticket = srt.ticket_info(is_resv[0]))
            else: 
                break
        time.sleep(1)
    print(is_resv)

if __name__=="__main__":
    main()