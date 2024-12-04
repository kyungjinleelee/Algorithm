# 입력 처리
n = int(input())
schedules = [tuple(map(int, input().split())) for _ in range(n)]

def max_profit(n, schedules):
    # Ti와 Pi를 분리하여 저장
    T = [0] * (n + 1)
    P = [0] * (n + 1)
    dp = [0] * (n + 2)  # n+1일째 이후에도 접근 가능하도록 크기 설정

    for i in range(1, n + 1):
        T[i], P[i] = schedules[i - 1]

    # 역순으로 DP 계산
    for i in range(n, 0, -1):
        if i + T[i] <= n + 1:  # 상담이 퇴사일을 넘지 않는 경우
            dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
        else:  # 상담이 퇴사일을 넘는 경우
            dp[i] = dp[i + 1]

    return dp[1]

print(max_profit(n, schedules))