import math

def solution(n, m):
    gcd_value = math.gcd(n, m)
    lcm_value = abs(n * m) // gcd_value
    
    return [gcd_value, lcm_value]