def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
    return answer

'''
이렇게도 풀 수 있음
intersection = set(s1) & set(s2)
return len(intersection)
'''