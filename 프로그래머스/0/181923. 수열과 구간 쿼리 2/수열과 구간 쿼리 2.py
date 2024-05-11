def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        min_val = int(1e9)
        
        for i in range(s, e + 1):
            if arr[i] > k:
                min_val = min(min_val, arr[i])
        if min_val != int(1e9):
            answer.append(min_val)
        else:
            answer.append(-1)
    return answer