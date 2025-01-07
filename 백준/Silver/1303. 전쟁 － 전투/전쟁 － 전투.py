from collections import deque
n, m = map(int, input().split())

field = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
# print(visited) # 5 * 5 2차원 false 배열

def bfs(x, y, team):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1  # 현재 병사 그룹의 크기

    # 상하좌우 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # 경계 검사 및 팀 일치 여부 확인
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and field[nx][ny] == team:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt

white_power = 0
blue_power = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            team = field[i][j]
            group_size = bfs(i, j, team)
            power = group_size ** 2
            if team == 'W':
                white_power += power
            else:
                blue_power += power

print(white_power, blue_power)