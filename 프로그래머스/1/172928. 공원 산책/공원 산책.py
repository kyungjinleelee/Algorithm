def solution(park, routes):
    # 공원의 크기
    h = len(park)
    w = len(park[0])
    
    # 시작 위치 탐색
    start = None
    for y in range(h):
        for x in range(w):
            if park[y][x] == "S":
                start = (y, x)
                break
        if start:
            break
    
    # 방향별 이동 벡터
    directions = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    # 초기 위치
    y, x = start
    
    # 명령 처리
    for route in routes:
        op, n = route.split()
        n = int(n)
        dy, dx = directions[op]
        
        # 이동 가능 여부 확인
        ny, nx = y, x
        valid_move = True
        for _ in range(n):
            ny += dy
            nx += dx
            if not (0 <= ny < h and 0 <= nx < w) or park[ny][nx] == "X":
                valid_move = False
                break
        
        # 이동 수행
        if valid_move:
            y, x = ny, nx
    
    return [y, x]