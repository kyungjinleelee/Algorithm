def solution(n):
    answer = 0
    count = 0
    
    while n > 0:
        answer += 1
        if '3' in str(answer) or answer % 3 == 0:
            continue
        count += 1
        
        if count == n:
            break
    return answer