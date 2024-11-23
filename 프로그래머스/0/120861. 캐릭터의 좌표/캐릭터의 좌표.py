def solution(keyinput, board):
    # 방향에 따른 이동 정의
    direction = {
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0)
    }
    
    # 초기 좌표
    x, y = 0, 0
    
    # 맵의 경계
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    # 키 입력 처리
    for key in keyinput:
        dx, dy = direction[key]
        new_x = x + dx
        new_y = y + dy
        
        # 경계를 벗어나지 않는 경우만 이동
        if -x_limit <= new_x <= x_limit and -y_limit <= new_y <= y_limit:
            x, y = new_x, new_y
    
    return [x, y]