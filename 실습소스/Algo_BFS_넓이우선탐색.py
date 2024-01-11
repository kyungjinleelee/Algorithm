"""
BFS 구현 방법
1. 루트 노드를 큐에 넣는다.
2. 현재 큐의 노드를 빼서 visited에 추가한다.
3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
4. 2부터 반복한다.
5. 큐가 비면 탐색 종료한다.
"""
from collections import deque

graph = {
	1: [2, 3, 4],
	2: [5],
	3: [5],
	4: [],
	5: [6, 7],
	6: [],
	7: [3],
}

def bfs_queue(start):
	visited = [start]	# 처음 시작점 visited에 넣어줌
	q = deque([start])	# 처음 시작점 q에 넣어줌

	while q:			# q가 빌 때까지 계속 반복
	    node = q.popleft()		# 제일 앞에 있는 녀석 꺼냄
	    for adj in graph[node]:	# 인접 노드를 살펴봄
		if adj not in visited:	# 인접 노드가 방문한 적이 없으면,
			q.append(adj)	# q의 방문 목록에 포함시키고
			visited.append(adj) # 방문 표시 해줌

	return visited

assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]	# '1부터 방문했을 때는 1, 2, 3, 4, 5, 6, 7 이 순서대로 방문해야 해'라는 테스트코드
