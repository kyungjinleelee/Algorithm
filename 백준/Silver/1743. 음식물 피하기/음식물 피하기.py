from collections import deque

# 입력 처리
import sys
input = sys.stdin.read

data = input().split()  # 한 번에 입력을 받아서 처리

N, M, K = map(int, data[:3])  # 첫 줄에서 N, M, K 읽기
trash_positions = list(map(int, data[3:]))  # 이후의 좌표를 읽음

grid = [[0] * M for _ in range(N)]  # 공원 격자 초기화

# 쓰레기 위치 설정
for i in range(K):
    r, c = trash_positions[2 * i] - 1, trash_positions[2 * i + 1] - 1
    grid[r][c] = 1  # 음식물 쓰레기 표시

# 이동 방향 (상하좌우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 구현
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    grid[start_x][start_y] = 0  # 방문 처리
    size = 1  # 현재 음식물 크기

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 격자 범위 내에 있고 음식물이 있는 경우
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))
                size += 1

    return size

# 탐색 및 최대 크기 계산
max_size = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:  # 음식물 쓰레기 발견 시
            max_size = max(max_size, bfs(i, j))

# 출력
print(max_size)