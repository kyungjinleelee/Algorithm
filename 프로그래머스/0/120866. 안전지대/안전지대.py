def solution(board):
    n = len(board)
    # 지뢰가 있는 위치 인덱스
    bomb = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb.append((i, j))
    
    # 지뢰 주변 8칸 위험 지역으로 표시
    for (x, y) in bomb:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                # 유효한 인덱스인지 확인 & 안전한 곳인지 확인
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    board[nx][ny] = -1
                        
    # 안전한 지역의 수 계산
    safe_place = sum(row.count(0) for row in board)
    
    return safe_place