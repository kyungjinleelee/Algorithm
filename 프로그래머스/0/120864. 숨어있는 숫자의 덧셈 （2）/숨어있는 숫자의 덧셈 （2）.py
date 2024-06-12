def solution(my_string):
    answer = 0
    curr_num = ''
    
    for i in my_string:
        if i.isdigit():
            curr_num += i
        else:
            if curr_num:
                answer += int(curr_num)
                curr_num = ''
                
    if curr_num:
        answer += int(curr_num)
    return answer