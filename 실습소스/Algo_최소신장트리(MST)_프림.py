# 최소 신장 트리(Minimum Spanning Tree, MST)
# 주요 알고리즘 : 프림, 크루스칼
"""
프림 작동 순서 
1. 임의의 정점을 시작으로 선택한다.
2. 해당 정점과 연결된 간선을 탐색 대상에 추가한다.
3. 탐색 대상에서 가장 가중치가 낮은 간선을 뽑는다. 
    간선의 끝 점이 아직 방문하지 않았다면, 그 간선을 추가한다.
   방문했다면, 방문하지 않은 간선이 나올 때까지 간선을 뽑는다.
4. 새로 추가된 정점과 연결된 간선을 탐색 대상에 추가한다.
5. 3-4번 과정을 (전체 정점 -1) 개의 간선이 트리에 추가될 때까지 반복한다.
"""
# 구현
def prim(n, edges) -> int:
   	"""
    	n: 정점의 개수
    	edges: (정점1, 정점2, 가중치)(로 묶여있는 튜플)의 리스트
	예시: 1번 - 2번 잇는 간선의 가중치가 5이다 -> (1, 2, 5) (또는 (2, 1, 5))

    	최소 스패닝 트리의 가중치를 반환
    	"""
	import heapq	# 계속 변화하는 탐색 대상에서 빠르게 최솟값을 뽑아낼 수 있기에 heap구조 사용 

	graph = [[] for _ in range(n + 1)]	# 2차원 리스트 만듦
	for idx, adj, cost in edges:		# idx: 정점 1, adj: 정점 2, cost: 가중치
		graph[idx].append((cost, adj))
		graph[adj].append((cost, idx))

	# 1. 임의의 정점을 시작으로 선택한다.
	visited = [False] * (n + 1)	# visited: 이 트리에 어떤 정점이 추가됐다를 알려줄 변수
	visited[1] = True		# 1번 추가 (1번 정점에서 시작)
	heap = []			# 빈 heap을 만들어줌, 우리가 탐색할 간선을 이 heap에 추가해 줄 것임
	for cost, adj in graph[1]:	# graph[1]에서 cost, adj를 뽑아가면서 반복 
		heapq.heappush(heap, (cost, adj))  # 2. 해당 정점과 연결된 간선을 탐색 대상에 추가한다.

	result = 0
	used_edges = 0
	while used_edges < n - 1:	# used_edges가 n-1보다 작을 동안 반복
		# 3. 가중치 낮은 간선을 선택한다.
		cost, idx = heapq.heappop(heap)
		# idx가 이미 방문한 정점이라면 패스
		if visited[idx]:
			continue
		# 방문하지 않은 경우
		visited[idx] = True	# 방문 체크 후
		result += cost		# 이 간선을 사용 할 거니까 result에 cost만큼 값 추가
		used_edges += 1		# used_edges를 1개 늘려줌
		# 4. 선택한 정점과 연결된 간선을 우선순위 큐에 넣는다. (= 탐색 대상에 추가한다)
		for adj_cost, adj in graph[idx]:	# idx: 선택한 정점, adj_cost: 연결된 간선
			if not visited[adj]:
				heapq.heappush(heap, (adj_cost, adj))

	return result
