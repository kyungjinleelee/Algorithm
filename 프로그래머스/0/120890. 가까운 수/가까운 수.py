def solution(array, n):
    minus = []
    answer = []
    
    for num in array:
        minus.append(abs(n - num))
        
    for i in range(len(minus)):
        if minus[i] == min(minus):
            answer.append(array[i])
    return int(min(answer))
        
    