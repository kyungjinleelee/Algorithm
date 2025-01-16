from collections import defaultdict
import math

def solution(fees, records):
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    # 차량 별 입/출차 기록 저장 
    parking_records = defaultdict(list)
    for record in records:
        time, car_number, action = record.split()
        parking_records[car_number].append(time)
    # print(parking_records) #'5961': ['05:34', '07:59', '22:59', '23:00']
    
    # 차량 별 누적 주차 시간 계산 (딕셔너리 원소 순회)
    total_time = {}
    for car, times in parking_records.items():
        total_minutes = 0
        
        for i in range(0, len(times), 2):
            in_time = times[i]
            out_time = times[i + 1] if i + 1 < len(times) else "23:59"
            
            # 시:분 -> 분으로 변환
            in_hour, in_minute = map(int, in_time.split(":"))
            out_hour, out_minute = map(int, out_time.split(":"))
            total_minutes += (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)
            
        total_time[car] = total_minutes
        
    # 요금 계산
    def calculate_fee(minutes):
        if minutes <= basic_time:
            return basic_fee
        else:
            extra_time = minutes - basic_time
            return basic_fee + math.ceil(extra_time / unit_time) * unit_fee
        
    
    # 차량 번호 오름차순 정렬 후 요금 계산
    answer = []
    for car in sorted(total_time.keys()):
        fee = calculate_fee(total_time[car])
        answer.append(fee)
        
    return answer