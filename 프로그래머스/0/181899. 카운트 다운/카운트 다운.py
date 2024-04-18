def solution(start_num, end_num):
    # 1. range 함수를 사용해서 start_num부터 end_num까지 감소하는 범위 생성
    # 2. list로 변환 
    return list(range(start_num, end_num - 1, -1))