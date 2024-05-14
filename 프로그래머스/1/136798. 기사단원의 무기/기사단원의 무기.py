def solution(number, limit, power):
    divisor_count = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisor_count[j] += 1
        
    for idx in range(1, number + 1):
        if divisor_count[idx] > limit:
            divisor_count[idx] = power
            
    return sum(divisor_count)