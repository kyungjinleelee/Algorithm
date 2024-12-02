from collections import deque
import sys
input = sys.stdin.readline

# 보드의 세로 크기 N, 가로 크기 M 입력 받기
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

# 주어진 입력 값에서 빨간 공의 위치와 파란 공의 위치를 반환
def getPos():
    rx, ry, bx, by = 0, 0, 0, 0
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                rx, ry = x, y
            if board[x][y] == 'B':
                bx, by = x, y
    return rx, ry, bx, by

# 각 공이 구멍 전까지 도달하는데 걸리는 기울이기 횟수를 구하기
def move(x, y, dx, dy):
    move_cnt = 0
    # 이동하는 위치가 벽이 아니고, 구멍에 들어가지 않을 동안 반복
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_cnt += 1
    return x, y, move_cnt

# bfs로 빨강 공이 구멍에 도달하면 result를 반환
def bfs():
    rx, ry, bx, by = getPos()

    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited.append((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, result = q.popleft()

        if result > 10: # 10번 초과 시 -1 리턴
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 구멍에 들어갈 경우
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 들어갈 경우 성공
            if board[nrx][nry] == 'O':
                print(result)
                return
            # 둘이 겹쳐있을경우 더 많이 이동한녀석을 1칸 뒤로 보낸다.
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 탐색하지 않은 방향 탐색
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, result + 1))
    print(-1)

bfs()