def matrix_mult(A, B, mod):
    """행렬 A와 B를 곱하고 각 원소를 mod로 나눈 나머지를 반환"""
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod
    return result

def matrix_power(A, B, mod):
    """행렬 A의 B제곱을 구하는 함수 (분할정복 사용)"""
    N = len(A)
    # 항등 행렬 생성
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    
    while B > 0:
        if B % 2 == 1:  # B가 홀수인 경우
            result = matrix_mult(result, A, mod)
        A = matrix_mult(A, A, mod)  # A를 제곱
        B //= 2
    return result

# 입력 처리
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
mod = 1000

# 계산
result = matrix_power(A, B, mod)

# 출력
for row in result:
    print(' '.join(map(str, row)))