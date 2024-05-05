def solution(arr):
    idx = idx2 = 0
    
    for i in range(len(arr)):
        if arr[i] == 2:
            idx = i
            break
    
    for j in range(len(arr) -1, -1, -1):
        if arr[j] == 2:
            idx2 = j
            break
    
    # 예외 처리
    if 2 not in arr:
        return [-1]
    
    return arr[idx:idx2+1]