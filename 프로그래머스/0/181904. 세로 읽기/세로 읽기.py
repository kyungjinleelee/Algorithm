def solution(my_string, m, c):
    splits = []
    answer = ''
    
    # my_string을 m개씩 끊어서 문자열에 저장
    for i in range(0, len(my_string), m):
        split = my_string[i:i+m]
        splits.append(split)

    for j in range(len(splits)):
        answer += splits[j][c-1]
    return answer
    
