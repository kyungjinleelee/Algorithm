def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        # finished[i]가 False 인 경우 
        if not finished[i]:
            answer.append(todo_list[i])
    return answer
            