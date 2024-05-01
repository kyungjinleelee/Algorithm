def solution(intStrs, k, s, l):
    answer = []
    for char in intStrs:
        a = int(char[s:s+l])
        if a > k:
            answer.append(a)
    return answer