def solution(str_list, ex):
    # 필터링 된 리스트 생성
    filtered_list = [s for s in str_list if ex not in s]
            
    # 필터링 된 문자열들을 순서대로 합친 후 반환
    return ''.join(filtered_list)
