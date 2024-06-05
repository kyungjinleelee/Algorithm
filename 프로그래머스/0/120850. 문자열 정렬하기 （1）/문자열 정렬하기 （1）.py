def solution(my_string):
    answer = []
    for str in my_string:
        if str.isdigit():
            answer.append(int(str))
    return sorted(answer)