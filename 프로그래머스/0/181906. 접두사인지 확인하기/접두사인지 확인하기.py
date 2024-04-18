def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(my_string)):
        # my_string의 각 인덱스까지의 부분 문자열이 is_prefix와 같으면 answer를 1로 갱신
        if my_string[:i+1] == is_prefix:
            answer = 1
            break
    return answer
'''
방법 2.
if my_string.startswith(is_prefix):
    return 1
else:
    return 0
'''
                