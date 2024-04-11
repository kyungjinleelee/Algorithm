def solution(a, b):
    if (a % 2 == 1 and b % 2 == 1):
        return a*a + b*b
    
    if (a % 2 == 0 and b % 2 == 1):
        return 2 * (a + b)
    
    if (a % 2 == 1 and b % 2 == 0):
        return 2 * (a + b)
    
    return abs(a - b)
