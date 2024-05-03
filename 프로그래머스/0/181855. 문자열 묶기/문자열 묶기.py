def solution(strArr):
    group_counts = {}
    
    for s in strArr:
        length = len(s)
        # length가 딕셔너리의 키로 존재하지 않는다면, 새로운 키로 추가하고 값을 1로 설정
        if length not in group_counts:
            group_counts[length] = 1
        # 존재하면 해당 키의 값에 1 추가
        else:
            group_counts[length] += 1
            
    return max(group_counts.values())