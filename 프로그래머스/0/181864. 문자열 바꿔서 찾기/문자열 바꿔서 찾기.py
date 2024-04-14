def solution(myString, pat):
    modified_string = ''
    
    # 문자열을 한 문자씩 검사해서 교체
    for char in myString:
        if char == 'A':
            modified_string += 'B'
        elif char == 'B':
            modified_string += 'A'
    
    # pat 유무에 따라 반환
    if pat in modified_string:
        return 1
    else:
        return 0