# 체스판 위의 나이트가 특정 위치에서 출발하여 목적지까지 최소 이동 횟수를 구하는 문제.
# 유형: bfs/dfs (최소 이동이면 bfs로 하자)
# 조건: 체스판은 8*8 사이즈. 

# 풀이 1 ============================================================
"""
- 이동할 수 있는 좌표를 dr, dc 변수에 만들어준다.
- 기본 bfs코드를 작성
-  r, c를 popleft() 로 꺼내준 다음에 r과 c가 이동하려는 좌표인지 체크해준다. 
    만약 방문하고자 하는 곳이면 visited[r][c]에 저장된 값에서 -1을 출력해준다. 
- 테스트케이스가 여러번 존재하는데 
  밖에서 bfs돌기전에 현재좌표와 목표좌표가 같은지 조사해주고, 만약 같다면 print(0) 해주면 좀더 시간복잡도를 줄일 수 있다. 
"""
import sys
input = sys.stdin.readline
test = int(input())

x = [1, -1, 1, -1, 2, -2, 2, -2]    # 이동가능한 8가지 방향
y = [2, 2, -2, -2, 1, 1, -1, -1]

def bfs(c_x, c_y):              # c_x, c_y: 현재 탐색 중인 위치 좌표
    q = []
    q.append((c_x, c_y))        # 첫 시작 지점을 q에 삽입
    c[c_x][c_y] += 1            # c 값을 1로 설정
    while q:        # q가 빌 때까지 반복 
        c_x, c_y = q.pop(0)       # q에서 원소 하나 꺼내서 현재위치로 설정
        if c_x == e_x and c_y == e_y:    # 시작, 목표위치가 같을 경우 
            return c[c_x][c_y]           # 정답을 찾음 > while문 종료 (예외처리)
        for dx, dy in zip(x, y):    # zip을 활용, 두 iterable 객체 한 번에 반복 
            nx = c_x + dx        # 다음 탐색할 x 좌표    
            ny = c_y + dy        # 다음 탐색할 y 좌표
            # x, y좌표가 탐색 가능한 위치에 있고, 아직 방문하지 않은 곳(-1)일 경우
            if 0 <= nx < size and 0 <= ny < size and c[nx][ny] == -1:
                q.append((nx, ny))    # 큐에 삽입하여 탐색
                c[nx][ny] = c[c_x][c_y] + 1 #거리 갱신
                
for _ in range(test):       # 테스트케이스의 수 입력받기
    size = int(input())        # 체스판의 크기 입력받기
    c = [[-1] * size for _ in range(size)]  # 크기=size인 2차원 배열 생성 > 모든 요소 -1로 초기화
    s_x, s_y = map(int, input().split())    # 시작 위치의 행과 열 
    e_x, e_y = map(int, input().split())    # 목표 위치의 행과 열
    print(bfs(s_x, s_y))

# 풀이 2 (모범답안)=======================================================

from sys import stdin
input = stdin.readline

def bfs(start: tuple[int, int], end: tuple[int, int], size: int) -> int:
    """
    input:
        start: 시작점 (x, y)
        end: 도착점 (x, y)
        size: 체스판 크기 n
    output:
        최소 이동 횟수
    """
    q = [start]				# 시작점(start)을 초기값으로 설정
    board = [[-1] * size for _ in range(size)]		# board: 방문 여부를 표시하기 위한 2차원 리스트 (visited같은 느낌), 초기값은 -1로 설정 (-1은 임의의 값임)
    board[start[0]][start[1]] = 0			# 현재 위치(시작점)의 좌표 = start[0]start[1]에는 0 설정 (0번이면 갈수있다)
    for x, y in q:			# q에서 좌표를 하나씩 꺼내면서 현재 위치에서 갈 수 있는 모든 이동 방향을 확인함
        if (x, y) == end:		# 좌표(x, y)가 우리가 원하는 끝점(end)이라면 
            return board[x][y]		# board[x][y] 반환 (= (x, y)까지 가는데 걸리는 시간 반환)
	# 끝점이 아니라면,
        for i in range(8):		# 현재 위치 (x, y)에서 가능한 8개의 이동 방향에 대해 반복
            nx, ny = x + dx[i], y + dy[i]  # 현재 위치 (x, y)에서 dx[i], dy[i]만큼 이동한 위치 (nx, ny)를 계산
            if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == -1:  # 만약 체스판 범위 내에 있고, 도착 못한 점이라면 (=-1)
                board[nx][ny] = board[x][y] + 1		# 방문 처리(현재까지 이동 횟수에 +1 하여 해당 위치까지의 최소 이동 횟수를 표시)
                q.append((nx, ny))			# 방문한 위치를 q에 추가 (나중에 해당 위치에서 다시 반복할 수 있도록 함)


dx = [2, 2, 1, 1, -1, -1, -2, -2]	# 나이트의 이동 방향을 나타내는 리스트
dy = [1, -1, 2, -2, 2, -2, 1, -1]
for _ in range(int(input())):		# 테스트케이스의 수 입력받기
    n = int(input())			# 체스판 크기 입력받기
    ix, iy = map(int, input().split())	# 시작점 입력받기
    fx, fy = map(int, input().split())	# 끝점 입력받기
    print(bfs((ix, iy), (fx, fy), n))	# bfs 함수 호출 
