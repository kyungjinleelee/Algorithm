def solution(n):
    # n*n 크기의 2차원 배열 만들기
    arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        # 대각선 위치 (i == j)에는 1 대입
        arr[i][i] = 1
    return arr