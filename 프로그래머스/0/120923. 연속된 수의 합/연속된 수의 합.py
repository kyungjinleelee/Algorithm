def solution(num, total):
    # 중간 값 구하기
    mid_num = total // num
    # 시작점 결정
    start = mid_num - (num - 1) // 2
    
    # 시작값부터 num개의 연속된 수를 생성하여 리스트로 반환
    return [start + i for i in range(num)]