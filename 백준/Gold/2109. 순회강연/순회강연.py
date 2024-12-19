n = int(input()) # 학교의 수
requests = [tuple(map(int, input().split())) for _ in range(n)] # 요청

def max_speech_fee(n, requests):
    # 강연 요청을 강연료 기준 내림차순 정렬
    requests.sort(key=lambda x: -x[0])
    # print(requests) # [(100, 2), (50, 10), (20, 1), (10, 3), (8, 2), (5, 20), (2, 1)]

    # 최대 날짜를 기준으로 강연 가능 여부 관리
    # max_day = max(request[1] for request in requests)
    max_day = 10000
    schedule = [False] * (max_day + 1)  # 각 날짜의 강연 여부 (총 20개)
    # print(schedule) [False, ...]

    total_fee = 0
    # 강연 요청 처리
    for p, d in requests:
        # d부터 거꾸로 탐색하며 가능한 날짜 찾기
        for day in range(d, 0, -1): # d 부터 거꾸로 탐색
            # print(day)
            if not schedule[day]:
                schedule[day] = True
                total_fee += p
                break # 강연을 배치했으므로, 더 탐색할 필요 없이 종료
    print(total_fee)

max_speech_fee(n, requests)