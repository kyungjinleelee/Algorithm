def solution(numbers):
    numbers.sort()
    
    max_answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
    
    return max_answer