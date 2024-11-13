def solution(common):
    # 첫 번째와 두 번째 원소의 차이를 구함 (공차)
    diff = common[1] - common[0]
    
    # 첫 번째와 두 번째 원소의 비율을 구함 (공비), 첫 번째 원소가 0인 건 공비 계산 예외 처리
    if common[0] != 0:
        ratio = common[1] // common[0]
    else:
        ratio = None
    
    # 등차수열인지 확인
    if common[2] - common[1] == diff:
        return common[-1] + diff
    # 그렇지 않은 경우는 등비수열
    else:
        return common[-1] * ratio