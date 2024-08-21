import itertools

def solution(number):
    comb = itertools.combinations(number, 3)
    
    answer = 0
    for c in comb:
        if sum(c) == 0:
            answer += 1
    return answer