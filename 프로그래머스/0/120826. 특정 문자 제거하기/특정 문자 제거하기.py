def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer

# return my_string.replace(letter, '') 이렇게도 가능