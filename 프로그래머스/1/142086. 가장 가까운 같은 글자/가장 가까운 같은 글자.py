def solution(s):
    other_str = []
    result = []
    for i in range(len(s)):
        if s[i] not in other_str:
            result.append(-1)
            other_str.append(s[i])
        else:
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    result.append(i-j)
                    break
    return result