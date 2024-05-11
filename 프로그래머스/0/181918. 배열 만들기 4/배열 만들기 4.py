def solution(arr):
    stk = [] 
    i = 0

    while i < len(arr):
        if not stk: # stk가 빈 배열인 경우
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    
    return stk