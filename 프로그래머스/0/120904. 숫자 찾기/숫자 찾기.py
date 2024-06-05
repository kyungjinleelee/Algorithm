def solution(num, k):
    str_k = str(k)
    str_num = str(num)
    
    if str_k in str_num:
        return str_num.index(str_k) + 1
    else:
        return -1