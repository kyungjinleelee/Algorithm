def solution(myString):
    answer = myString.split('x')
    without_spaces = [x for x in answer if x.strip()]
    return sorted(without_spaces)