def solution(names):
    # 빈 리스트인 groups를 생성 
    groups = []
    # 주어진 리스트 names를 5명씩 묶어서 groups에 추가
    for i in range(0, len(names), 5):
        groups.append(names[i:i+5])
        
    result = []
    # 맨 앞 사람 새로운 리스트에 담기
    for group in groups:
        result.append(group[0])
    # 새로운 리스트 반환
    return result

    # 리스트 컴프리헨션으로 한 줄로 반환할 수도 있음
    # return [group[0] for group in groups]

