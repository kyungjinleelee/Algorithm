def solution(t, p):
    answer = 0
    len_p = len(p)
    
    for i in range(len(t)):
        slice_char = t[i:i+len_p]
        if len(slice_char) == len_p and slice_char <= p:
            answer += 1
    return answer