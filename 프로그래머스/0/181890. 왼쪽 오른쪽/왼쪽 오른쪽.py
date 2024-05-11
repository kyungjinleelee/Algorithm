def solution(str_list):
    answer = []
    for i in range(len(str_list)):
        char = str_list[i]
        if char == 'l':
            answer = str_list[:i]
            break
        elif char == 'r':
            answer = str_list[i+1:]
            break
    return answer