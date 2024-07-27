def solution(n):
    answer = []
    for i in range(2, int(n ** 0.5) + 1):
        # n이 i로 나누어질 때 까지 반복
        while n % i == 0:
            # 중복 없이 저장되도록 조건 체크
            if i not in answer:
                answer.append(i)
            n //= i
            
    # 소수인 경우 예외처리
    if n > 1:
        answer.append(n)
    return answer