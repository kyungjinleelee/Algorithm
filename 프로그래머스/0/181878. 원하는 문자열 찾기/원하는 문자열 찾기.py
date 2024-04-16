def solution(myString, pat):
    myString_upper = myString.upper()
    pat_upper = pat.upper()
    if pat_upper in myString_upper:
        return 1
    else:
        return 0