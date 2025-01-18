N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열 초기화
answer = [[0] * M for _ in range(N)]
def plus(a, b):
    for i in range(N): # 행의 인덱스
        for j in range(M): # 열의 인덱스
            answer[i][j] = a[i][j] + b[i][j]

plus(a, b)

# 결과 출력
for row in answer:
    print(*row)