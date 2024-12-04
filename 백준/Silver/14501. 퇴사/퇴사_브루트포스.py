def max_profit(day, current_profit):
    global max_result

    # 퇴사일을 넘긴 경우 종료
    if day > n:
        # 최대 수익 갱신
        max_result = max(max_result, current_profit)
        return

    # 1. 현재 상담을 선택하지 않는 경우
    max_profit(day + 1, current_profit)

    # 2. 현재 상담을 선택하는 경우 (퇴사일 이전에 상담 완료 가능해야 함)
    if day + T[day] - 1 <= n:  # day부터 상담을 진행했을 때 퇴사일을 넘지 않는 경우
        max_profit(day + T[day], current_profit + P[day])


# 입력
n = int(input())  # 상담 가능한 날짜 수
T = [0] * (n + 1)  # 상담 기간
P = [0] * (n + 1)  # 상담 수익
for i in range(1, n + 1):
    T[i], P[i] = map(int, input().split())

max_result = 0
max_profit(1, 0)  # 첫 번째 날부터 탐색 시작
print(max_result)
