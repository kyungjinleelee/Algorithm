# 2차원 배열로 섬의 전체 지도가 주어질 때, 총 섬의 갯수를 구하는 문제
# 배열 내 1을 0으로 바꿔주고 상하좌우 인접 1이 없으면 cnt를 1씩 늘려주는 방식

# DFS ver
# 나는 stack을 이용

def island_dfs_stack(grid):
	dx = [0, 0, 1, -1]
	dy = [1, -1, 0, 0]
	rows, cols = len(grid), len(grid[0])	# rows: 행의 갯수, cols: 열의 갯수
	cnt = 0

	for row in range(rows):			  # rows와 cols 기준으로 이중 for문 돌면서 배열 순회
		for col in range(cols):
			if grid[row][col] != '1': # grid가 지금 방문한 곳이 문자열 1인지 아닌지 봄
			    continue		  # 1이 아니라면 지나감 
			
			# 섬 하나를 0으로 바꾸고 > 숫자 1 올리는 코드들
			cnt += 1		  # 1이라면 cnt 1 증가
			stack = [(row, col)]	  # 그리고 방문한 좌표를 stack에 넣음
		
			while stack:		  # stack이 비어있는 동안 (방문할 점이 남아있는 동안) 계속 while문 돎
				x, y = stack.pop() # stack에서 제일 위에 있는 점 꺼냄
				grid[x][y] = '0'   # 그 점을 0으로 바꿔줌
				for i in range(4): # 그 점의 상하좌우 방문
					nx = x + dx[i]
					ny = y + dy[i]
					# x가 범위를 넘어가거나 y가 범위를 넘어갈 때나 1이 아닌 경우에는 pass (스택에 안붙임)
					if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
					    continue
					stack.append((nx, ny))
	return cnt

# 테스트케이스
assert island_dfs_stack(grid=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1

assert island_dfs_stack(grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3

# ===================================== bfs =========================
# BFS ver (내 손에 코드 꼭 익혀보자!!!!!! 아이디어는 어려운 게 없음, 구현이 어려운 거임)
def island_bfs(grid):
	dx = [0, 0, 1, -1]
	dy = [1, -1, 0, 0]
	rows, cols = len(grid), len(grid[0])	# rows: 행의 갯수, cols: 열의 갯수
	cnt = 0					# 섬의 개수 0으로 초기화 

	for row in range(rows):			  # rows와 cols 기준으로 이중 for문 돌면서 배열 순회 (왼쪽 상단부터 오른쪽 하단까지)
		for col in range(cols):
			if grid[row][col] != '1': # grid가 지금 방문한 곳이 문자열 1인지 아닌지 봄
			    continue		  # 1이 아니라면 지나감 (=섬이 아니면 넘어감)
			
			# 섬 하나를 0으로 바꾸고 > 숫자 1 올리는 코드들
			cnt += 1		  # 1이라면 cnt 1 증가
			q = deque([(row, col)])	  # 그리고 방문한 좌표를 q의 시작으로 넣어줌
		
			while q:		  # q가 빌 때까지(방문할 점이 남아있는 동안) 계속 while문 돎
				x, y = q.popleft() # q에서 제일 앞에 있는 점 꺼냄
				for i in range(4): # 그 점의 상하좌우 방문
					nx = x + dx[i] # 신규 좌표 계산
					ny = y + dy[i]
					# 신규 좌표가 범위를 벗어나거나, 섬이 아닌 경우에는 pass 
					if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
					    continue
					grid[x][y] = '0'   # 맞다면, 방문 표시하고 (그 점을 0으로 바꿔줌)
					q.append((nx, ny)) # q에 넣어줌
	return cnt

# 테스트케이스
assert island_bfs(grid=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1

assert island_bfs(grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3
