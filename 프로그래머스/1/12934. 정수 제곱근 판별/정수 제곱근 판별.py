import math

def solution(n):
    # n의 제곱근을 구한 뒤 그 수를 다시 제곱해서 n이랑 비교
    sqrt_n = math.sqrt(n)
    
    if sqrt_n.is_integer():
        return (sqrt_n + 1) ** 2
    else:
        return -1