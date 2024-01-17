# 백준 10026 적록색약
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력하는 문제
# 구역은 N * N
# DFS 활용
def count_section(board: list[list[str]]) -> int:
    """
    input:
        board: 2차원 배열
    output:
        구역의 수
    """
    visited = [[False] * n for _ in range(n)]	# 방문표시 해 줄 n*n 행렬 만들어줌
    section = 0					# 전체 구역의 수
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for x in range(n):				# 왼쪽 위부터 탐색 시작
        for y in range(n):
            if not visited[x][y]:		# 현재 칸 (x, y)이 방문을 안했다면
                section += 1			# 신규 구역이 하나 늘어났다! (섹션값 1개 늘려줌)
                stack = [(x, y)]		# stack에 현재 좌표 넣어줌
                visited[x][y] = True		# 이 점에 방문처리 해줌
                target = board[x][y]		# 처음 출발한 위치의 색(board[x][y])을 기억해줌 (target = 초기색깔) 
                # dfs
                while stack:
                    cx, cy = stack.pop()
                    for i in range(4):		# 4방향으로 cx, cy 좌표에 대해서 탐색
                        nx, ny = cx + dx[i], cy + dy[i]
			# nx, ny가 격자판 안에 있고, 아직 방문 안했고, 방문하려는 칸(board[nx][ny])이 초기색깔과 같다면
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                            stack.append((nx, ny))	# stack에 append한 후
                            visited[nx][ny] = True	# 방문 처리
    return section	# section: 우리가 찾는 구역의 수 저장


n = int(input())			# 보드판 사이즈
board = [input() for _ in range(n)]	# 우리가 보는 격자판 
# 적록색약인 사람이 보는 구역의 수를 구하기 위해 G를 R로 바꿈 ★
new_board = [line.replace('G', 'R') for line in board]	# 적록색약이 보는 격자판
print(count_section(board), count_section(new_board))
