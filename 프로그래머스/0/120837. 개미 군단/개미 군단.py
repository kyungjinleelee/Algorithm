def solution(hp):
    answer = 0
    # 장군개미의 수
    answer += hp // 5
    hp %= 5
    # 병정개미의 수
    answer += hp // 3
    hp %= 3
    # 일개미의 수
    answer += hp // 1
    
    return answer