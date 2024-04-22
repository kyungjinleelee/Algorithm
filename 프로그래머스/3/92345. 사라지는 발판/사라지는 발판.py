dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 1e9

def solution(board, aloc, bloc):
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]

def in_range(board, y, x):
    if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]):
        return False
    return True

def is_finished(board, y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if in_range(board, ny, nx) and board[ny][nx]:
            return False
    return True

def solve(board, y1, x1, y2, x2):
    result = [False, 0]
    # 움직일 수 있는 공간이 없을 때
    if is_finished(board, y1, x1):
        return result

    # 현재 차례인데 둘이 같은 공간에 있음 (이번 턴에 움직이면 무조건 이김)
    if y1 == y2 and x1 == x2:
        return [True, 1]
    
    min_turn = INF
    max_turn = 0
    can_win = False

    # dfs
    # 구현
    for i in range(4):
        ny = y1 + dy[i]
        nx = x1 + dx[i]
        if not in_range(board, ny, nx) or not board[ny][nx]:
            continue
            
        board[y1][x1] = 0
        # 차례 바뀌기 때문에 위치 바꿔줌
        result = solve(board, y2, x2, ny, nx)
        board[y2][x2] = 1
            
        # 다음 턴에서 질 경우: 이번 턴 사람은 승리한다는 뜻이기 때문에 최솟값 저장 
        if not result[0]:
            can_win = True
            min_turn = min(min_turn, result[1])
        # 다음 턴에서 이길 경우: 이번 턴 사람은 진다는 뜻이기 때문에 최댓값 저장
        elif not can_win:
            max_turn = max(max_turn, result[1])
            
    turn = min_turn if can_win else max_turn
    # 다음에는 턴 수가 증가하므로 
    return [can_win, turn + 1]