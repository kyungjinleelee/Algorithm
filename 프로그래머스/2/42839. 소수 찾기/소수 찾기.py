from itertools import permutations

def is_sosu(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
    sosu = set()
    
    # 모든 가능한 숫자 조합 생성
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            num = int(''.join(perm))
            sosu.add(num)
            
    # 소수 판별해서 갯수 세기
    count = 0
    for num in sosu:
        if is_sosu(num):
            count += 1
            
    return count