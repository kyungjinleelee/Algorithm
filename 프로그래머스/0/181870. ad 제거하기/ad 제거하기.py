def solution(strArr):
    answer = []
    for char in strArr:
        if not "ad" in char:
            answer.append(char)
    return answer