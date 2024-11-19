from math import gcd

def solution(a, b):
    # 최대공약수를 이용해 기약분수로 변환
    divisor = gcd(a, b)
    reduced_denominator = b // divisor
    
    # 분모의 소인수에서 2와 5 제거
    for prime in [2, 5]:
        while reduced_denominator % prime == 0:
            reduced_denominator //= prime
    
    # 남은 값이 1이면 유한소수, 그렇지 않으면 무한소수
    return 1 if reduced_denominator == 1 else 2