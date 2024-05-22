def solution(arr, intervals):
    answers = []
    result = []
    for interval in intervals:
        s, e = interval
        answers = arr[s:e+1]
        for answer in answers:
            result.append(answer)    
    return result