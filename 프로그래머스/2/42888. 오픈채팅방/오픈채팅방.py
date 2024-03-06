def solution(record):
    answer = []
    nicknamesDB = dict()    # 유저 닉네임들 저장할 딕셔너리 선언
    actions = []            # Enter, Leave, Change 
    
    for event in record:
        info = event.split()    # ex) Enter uid1234 Muzi
        # action, userid
        action, userid = info[0], info[1]
        
        # nickname 
        #(action이 Leave일 경우 닉네임 정보 x)
        if action in ("Enter", "Change"):
            nickname = info[2]
            # Enter, Change일 경우 닉네임 변경 가능성 있기 때문에 DB에 저장/갱신
            nicknamesDB[userid] = nickname
        actions.append((action, userid))
        
    # actions에 저장된 정보 순회
    for actionInfo in actions:
        action, userid = actionInfo[0], actionInfo[1]
        if action == 'Enter':
            answer.append(f'{nicknamesDB[userid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{nicknamesDB[userid]}님이 나갔습니다.')
            
    return answer