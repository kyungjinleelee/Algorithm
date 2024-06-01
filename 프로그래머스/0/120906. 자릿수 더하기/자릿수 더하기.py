def solution(n):
    str_n = str(n)
    
    answer = []
    for i in str_n:
        answer.append(int(i))
    return sum(answer)