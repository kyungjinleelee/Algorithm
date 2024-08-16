def solution(price, money, count):
    total = 0
    
    for i in range(1, count + 1):
        total += price * i
    lack = money - total
    
    return abs(lack) if lack < 0 else 0
    