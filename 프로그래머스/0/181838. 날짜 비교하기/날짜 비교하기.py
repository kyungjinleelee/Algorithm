from datetime import datetime

def solution(date1, date2):
    # date1을 datetime 객체로 변환
    datetime1 = datetime(date1[0], date1[1], date1[2])
    # date2를 datetime 객체로 변환
    datetime2 = datetime(date2[0], date2[1], date2[2])
    
    # date1이 date2보다 앞선지 여부를 확인
    if datetime1 < datetime2:
        return 1
    else:
        return 0