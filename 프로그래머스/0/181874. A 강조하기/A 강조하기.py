def solution(myString):
    answer = ''
    for char in myString:
        if char == 'a' or char == 'A':
            answer += 'A'
        elif char.isupper():
            answer += char.lower()
        else:
            answer += char
    return answer
