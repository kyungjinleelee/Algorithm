def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    # 리스트를 모두 순회한 후에도 음수를 찾지 못할 시 -1 반환
    return -1