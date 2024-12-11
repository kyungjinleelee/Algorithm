N = int(input()) # 첫 줄: 소의 수 N

# 다음 N줄: 도착 시간 T, 검문 시간 W
cows = []
for _ in range(N):
    T, W = map(int, input().strip().split())
    cows.append((T, W))

def solution(N, cows):
    cows.sort() # 도착 시간 기준으로 정렬

    end_seconds = 0 # 현재 검문 끝나는 시간
    for T, W in cows:
        # 끝난 시간이랑 다음 도착 시간이랑 비교
        if end_seconds < T:
            end_seconds = T
        end_seconds += W
    return end_seconds

result = solution(N, cows)
print(result)