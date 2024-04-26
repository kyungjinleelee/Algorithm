def solution(n):
    # 초기값을 수열에 추가해줌
    answer = [n]
    
    # 초기값이 1이 될 때까지 반복
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1)
        answer.append(n)
    return answer