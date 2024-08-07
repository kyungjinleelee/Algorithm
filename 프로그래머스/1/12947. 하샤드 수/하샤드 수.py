def solution(x):
    list_x = list(str(x))
    hap = 0
    
    for i in list_x:
        hap += int(i)
    
    if x % hap == 0:
        return True
    return False