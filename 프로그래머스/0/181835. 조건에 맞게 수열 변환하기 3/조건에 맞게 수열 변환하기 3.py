def solution(arr, k):
    if k % 2 != 0:
        return [x * k for x in arr]
    elif k % 2 == 0: 
        return [x + k for x in arr]