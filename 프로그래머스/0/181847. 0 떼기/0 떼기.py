def solution(n_str):
    
    for i in range(len(n_str)):
        if n_str[i] != '0':
            # 0이 아닐 경우 i 부터 n_str 끝까지 반환
            return n_str[i:]

    # 문자열이 모두 0일 경우 빈 문자열만 반환
    return ''

print(solution("000123"))
print(solution("123123"))
print(solution("0000"))