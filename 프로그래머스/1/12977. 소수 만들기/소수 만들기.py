from itertools import combinations
import math

def solution(nums):
    answer = 0
    
    # 3개의 숫자를 선택하는 조합 생성
    comb = combinations(nums, 3)
    
    for c in comb:
        if is_prime(sum(c)):
            answer += 1
    return answer

# 소수 여부를 판별하는 함수
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True