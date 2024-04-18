def solution(num_list, n):
    # n번째 이후의 요소 구하기
    slice_list = num_list[:n]
    
    # n번째 까지의 원소 구하기 
    slice_list2 = num_list[n:]
    
    # 두 리스트 이어붙여서 반환
    return slice_list2 + slice_list