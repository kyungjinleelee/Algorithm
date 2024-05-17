def solution(l, r):
    answer = []
    
    for num in range(l, r+1):
        num_str = str(num)
        all_valid = True
        
        for ch in num_str:
            # 문자열 num_str의 각 문자가 '0' 또는 '5'가 아닌지 확인
            if ch not in '05':
                all_valid = False
                break
                
        if all_valid:
            answer.append(num)
            
    if not answer:
        return [-1]
    
    return sorted(answer)