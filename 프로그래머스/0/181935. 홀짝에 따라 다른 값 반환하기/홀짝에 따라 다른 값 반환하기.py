def solution(n):
    if n % 2 != 0:
        odd_sum = 0
        # 1부터 n까지의 홀수를 순회
        for i in range(1, n + 1, 2):
            odd_sum += i
        return odd_sum
    else:
        even_sum = 0
        # 2부터 n까지의 짝수를 순회
        for i in range(2, n + 1, 2):
            even_sum += (i ** 2)
        return even_sum
    
'''
리스트 컴프리헨션
if n % 2 != 0:
    return sum([i for i in range(1, n + 1, 2)])
else:
    return sum([i ** 2 for i in range(2, n + 1, 2)])
'''