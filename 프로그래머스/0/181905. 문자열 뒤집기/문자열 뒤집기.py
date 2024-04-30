def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
'''
my_string[s:e+1] : 인덱스 s부터 s까지 부분 문자열을 추출
[::-1] : 추출한 거 역순으로 뒤집음
'''