def solution(a, d, included):
    answer = 0
    
    # a부터 시작해서 d씩 더하는 등차수열
    sequence = list(range(a, a + d * len(included), d))
    
    for i in range(len(included)):
        if included[i] is True:
            answer += sequence[i]
    return answer