def solution(s):
    count_zero = 0
    count_binary = 0
    
    while s != '1':
        # 0의 갯수 카운트하고 s의 모든 0 제거
        count_zero += s.count('0')
        s = s.replace('0', '')
         
        # s를 s의 길이(c)를 2진법으로 표현한 문자열로 바꾸기
        c = len(s)
        binary_str = ''
    
        # 정수를 2로 나눠가면서 나머지를 구하고 이를 역순으로 연결
        while c > 0:
            binary_str += str(c % 2)
            c //= 2
            
        s = binary_str[::-1]
        count_binary += 1
    
    return [count_binary, count_zero]