def solution(my_string):
    answer = ''
    vowels = 'aeiou'
    
    for char in my_string:
        if char not in vowels:
            answer += char
    return answer