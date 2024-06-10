def solution(order):
    clap = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            clap += 1
    return clap