def solution(str_list, ex):
    filtered_list = []
    # 필터링 된 리스트 생성
    for s in str_list:
        if ex not in s:
            filtered_list.append(s)
            
    # 필터링 된 문자열들을 순서대로 합치기
    tail_string = ''.join(filtered_list)
    
    return tail_string