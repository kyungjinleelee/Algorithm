def solution(a, b):
    answer = 0
    concat_1 = int(str(a) + str(b))
    concat_2 = int(str(b) + str(a))
    return max(concat_1, concat_2)