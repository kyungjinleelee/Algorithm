def solution(arr, delete_list):
    answer = []
    
    for ele in arr:
        if ele not in delete_list:
            answer.append(ele)
    return answer