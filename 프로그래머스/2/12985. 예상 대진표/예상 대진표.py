def solution(n,a,b):
    answer = 0 
    while a != b:
        answer += 1
        a = (a + 1) // 2    # A의 다음 라운드 번호 계산
        b = (b + 1) // 2    # B의 다음 라운드 번호 계산

    return answer

# 예시 입력: 총 경기 참여자 수 N, 지원자 A, B
n = 8
a = 1
b = 5

# 두 지원자가 만날 때까지 걸리는 라운드 수 계산
answer = solution(n, a, b)
print("두 지원자가 만날 때까지 걸리는 라운드 수:", answer)