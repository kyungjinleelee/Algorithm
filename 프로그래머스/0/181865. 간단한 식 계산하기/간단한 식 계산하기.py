def solution(binomial):
    # 이항식을 공백을 기준으로 나눠서 숫자와 연산자를 분리
    a, op, b = binomial.split()
    a = int(a)
    b = int(b)
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b