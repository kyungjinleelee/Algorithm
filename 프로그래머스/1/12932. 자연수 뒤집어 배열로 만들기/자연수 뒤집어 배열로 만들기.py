def solution(n):
    answer = []
    digits = list(str(n))
    for i in range(1, len(digits) + 1):
        answer.append(int(digits[-i]))
    return answer