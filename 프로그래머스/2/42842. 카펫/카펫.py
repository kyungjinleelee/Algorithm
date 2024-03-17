def solution(brown, yellow):
    answer = []
    # 총 블록 수 (a * b = total)
    total = brown + yellow
    
    # a: 가로의 길이
    # b: 세로의 길이 
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:    # total / b = a
            a = total / b
            if a >= b:
                if 2*a + 2*b == brown + 4:
                    return [a, b]

    return answer 


"""
<조건>
a = 가로의 길이
b = 세로의 길이 

1. a >= b
2. 2a + 2b - 4 = brown
3. (a-2) * (b-2) = yellow
↓
2. 2a + 2b = brown + 4
3. ab - 2a - 2b + 4 = yellow

-> ab - brown - 4 + 4 = yellow
-> ab = yellow + brown
"""
