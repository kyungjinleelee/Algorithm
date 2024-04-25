def solution(number):
    integer = int(number)
    if integer > 0:
        return integer % 9
    elif integer == 0:
        return 0