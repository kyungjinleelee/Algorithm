import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n)
    
    if sqrt.is_integer():
        return 1
    else:
        return 2