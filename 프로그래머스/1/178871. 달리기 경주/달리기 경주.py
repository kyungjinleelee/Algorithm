def solution(players, callings):
    # 선수 이름 : 현재 등수(인덱스) 딕셔너리 생성
    idx = {name : i for i, name in enumerate(players)}
    
    for call in callings:
        # 추월한 선수의 현재 등수(인덱스)
        i = idx[call]
        # 바로 앞 선수와 자리 바꾸기
        players[i], players[i - 1] = players[i - 1], players[i]
        # 딕셔너리의 인덱스 정보 갱신
        idx[players[i]] = i
        idx[players[i - 1]] = i - 1
        
    return players