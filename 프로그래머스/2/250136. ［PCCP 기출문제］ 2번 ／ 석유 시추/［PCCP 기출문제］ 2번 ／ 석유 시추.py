from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]  # 방문 처리를 위한 2차원 배열

    # 현재 위치에서 상하좌우로 연결된 기름 덩어리들을 탐색하는 bfs
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        size = 1  # 초기화
        while queue:
            cur_x, cur_y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cur_x + dx, cur_y + dy
                # 현재 x, y좌표가 유효 범위에 있는지, 방문했는지 여부 검사
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] or land[nx][ny] == 0:
                    continue
                # 방문 표시 및 연결된 석유 카운트
                visited[nx][ny] = True
                size += 1
                queue.append((nx, ny))
        return size

    max_oil = 0
    # 모든 석유 덩어리 크기 계산 (석유가 있고 방문하지 않았으면 bfs 호출)
    for col in range(m):
        current_oil = 0
        visited = [[False] * m for _ in range(n)]
        for row in range(n):
            if land[row][col] == 1 and not visited[row][col]:
                # 새로운 덩어리 발견
                chunk_size = bfs(row, col)
                current_oil += chunk_size
        max_oil = max(max_oil, current_oil)
    return max_oil