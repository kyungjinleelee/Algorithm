from math import gcd

def solution(numer1, denom1, numer2, denom2):
    # 두 분수의 합을 계산
    numerator = numer1 * denom2 + numer2 * denom1  # 분자
    denominator = denom1 * denom2                 # 분모
    
    # 최대공약수를 이용해 기약 분수로 변환
    divisor = gcd(numerator, denominator)
    numerator //= divisor
    denominator //= divisor
    
    return [numerator, denominator]