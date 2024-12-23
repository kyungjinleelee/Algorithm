from collections import deque
import sys

input = sys.stdin.readline

# 상하좌우 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = [list(input().rstrip()) for _ in range(12)]
# 연쇄 횟수
combo = 0


# 상하좌우로 동일한 블록들을 탐색해 해당 좌표들을 가진 리스트를 반환
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    same_blocks = [(x, y)]  # 동일한 블록의 좌표를 저장할 리스트

    while q:
        x, y = q.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 좌표가 범위 안에 있고, 아직 방문하지 않은 좌표이며, 같은 색의 뿌요인지?
            if 0 <= nx < 12 and 0 <= ny < 6 and board[x][y] == board[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                same_blocks.append((nx, ny))
    return same_blocks


# 동일한 블록들의 집합을 . 으로 변경
def delete(same_blocks):
    for x, y in same_blocks:
        board[x][y] = "."

# 역순으로 반복문을 돌며 위에서 아래로 블록을 내림
def applying_gravity():
    for y in range(6):
        for x in range(10, -1, -1): # 아래에서 위로 탐색
            for k in range(11, x, -1): # 아래쪽으로 블록을 내림
                if board[x][y] != "." and board[k][y] == ".":
                    board[k][y] = board[x][y]
                    board[x][y] = "."

while True:
    pang = False
    # 매 턴마다 방문 배열 초기화
    visited = [[False] * 6 for _ in range(12)]

    for x in range(12):
        for y in range(6):
            if board[x][y] != "." and not visited[x][y]:
                same_blocks = bfs(x, y)

                # 동일한 블록이 4개이상일 경우 블록을 터트림
                if len(same_blocks) >= 4:
                    pang = True
                    delete(same_blocks)

    # 블록을 터트렸다면 중력 적용 후 -> 콤보 증가
    if pang:
        applying_gravity()
        combo += 1
    # 터트릴 블록 없으면 종료
    else:
        break

print(combo)