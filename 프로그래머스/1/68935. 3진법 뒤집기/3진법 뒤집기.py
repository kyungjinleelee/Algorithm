def solution(n):
    # 10진수 -> 3진법으로 변환
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
        
    # 뒤집기
    reverse_ternary = ternary[::-1]
    
    # 다시 3진법 -> 10진법 변환
    answer = int(reverse_ternary, 3)
    return answer