def solution(a, b, n):
    total_cola = 0
    
    while n >= a:
        new_cola = (n // a) * b  # 콜라 병 수
        total_cola += new_cola   # 받은 콜라 추가
        n = (n % a) + new_cola   # 남은 병 + 새로 받은 콜라 병
    return total_cola