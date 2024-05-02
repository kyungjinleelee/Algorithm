def solution(myString, pat):
    max_substr = ''
    
    # 역순으로 순회
    for i in range(len(myString)-1, -1, -1):
        if myString[i:].startswith(pat):
            substr = myString[0:i+len(pat)]
            if len(substr) > len(max_substr):
                max_substr = substr
                
    return max_substr