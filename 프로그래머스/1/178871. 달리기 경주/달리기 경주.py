def solution(players, callings):
    # 선수 이름을 키로, 현재 등수를 값으로 저장하는 딕셔너리
    player_positions = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        curr_position = player_positions[call]   # 추월한 선수의 현재 위치
        
        # 앞에 있는 선수와의 자리 교환
        if curr_position > 0:
            front_player = players[curr_position - 1]
            
            # 자리 교환
            players[curr_position - 1], players[curr_position] = players[curr_position], players[curr_position - 1]
            
            # 딕셔너리에서 두 선수의 위치 정보 업데이트
            player_positions[call] -= 1
            player_positions[front_player] += 1
    
    return players