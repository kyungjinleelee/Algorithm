def solution(num_list):
    answer = []
    sort = sorted(num_list)
    for i in range(len(sort)):
        if i >= 5 and i <= len(sort):
            answer.append(sort[i])
    return answer