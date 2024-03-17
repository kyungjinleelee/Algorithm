def solution(brown, yellow):
    answer = []
    # 총 블록 수 
    total = brown + yellow
    
    # a: 가로의 길이
    # b: 세로의 길이 
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:
            a = total / b
            if a >= b:
                if 2*a + 2*b == brown + 4:
                    return [a, b]

    return answer 
