def solution(clothes):
    dict = {}
    for value, key in clothes:
        if key in dict:
            dict[key].append(value)
        else:
            dict[key] = [value]

    answer = 1
    for key in dict:
        answer *= len(dict[key]) + 1
        
    # 아무것도 안 입는 경우는 제외하기 위해 -1
    answer -= 1
    return answer