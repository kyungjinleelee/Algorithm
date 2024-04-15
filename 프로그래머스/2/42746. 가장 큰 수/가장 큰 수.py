def solution(numbers):
    # 각 숫자를 문자열로 먼저 변환
    numbers = list(map(str, numbers))
    
    # 두 수를 이어붙였을 때 큰 숫자 순서대로 정렬
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    # 예외 처리 (모든 수가 0일 경우)
    if numbers[0] == '0':
        return '0'
    
    # 정렬된 숫자 이어붙이기 
    return ''.join(numbers)

print(solution([0, 10, 7]))
print(solution([5, 30, 5]))
print(solution([0, 0, 0]))