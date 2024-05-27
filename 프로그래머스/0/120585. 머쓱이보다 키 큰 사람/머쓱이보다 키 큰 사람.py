def solution(array, height):
    answer = sum(1 for i in array if i > height)
    return answer