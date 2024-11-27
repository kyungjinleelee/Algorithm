def solution(sides):
    a, b = sides
    '''
    삼각형을 만들기 위한 조건
    1. a + b > c (가장 긴 변이 c일 때)
    2. a + c > b (가장 긴 변이 b일 때)
    3. b + c > a (가장 긴 변이 a일 때)
    위 조건을 종합하면?
    |a - b| < c < a + b
    '''
    
    # 가능한 범위 계산
    min_c = abs(a - b) + 1
    max_c = a + b - 1
    
    # 정수 갯수
    return max_c - min_c + 1