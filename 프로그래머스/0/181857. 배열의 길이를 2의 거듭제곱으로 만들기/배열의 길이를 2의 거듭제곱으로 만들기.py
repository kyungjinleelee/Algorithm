def solution(arr):
    length = len(arr)
    for i in range(length):
        square = 2 ** i
        if len(arr) <= square:
            arr += [0] * (square - length)
            break
    return arr