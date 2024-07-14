def solution(numbers, k):
    n = len(numbers)
    index = ((k - 1) * 2) % n
    return numbers[index]