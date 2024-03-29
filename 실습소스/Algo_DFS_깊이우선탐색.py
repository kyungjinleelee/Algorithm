"""
DFS : 깊이우선탐색 (Depth First Search)
DFS 재귀적으로 짤 때 가장 중요한 아이디어
1. 반복적으로 발생하는 일이 뭔가를 아는 것
2. 종료 조건을 아는 것
"""
# 테스트 코드
from dfs_dfs.prac import dfs_recursive, dfs_stack

assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]		# 어떤 노드에서 출발할 건지(1) 지정만 해주면 나머지가 나온다

# 구현 코드 
graph = {
   1: [2, 3, 4],
   2: [5],
   3: [5],
   4: [],
   5: [6, 7],
   6: [],
   7: [3],
}


def dfs_recursive(node, visited):	# node: 내가 지금 방문한 노드, visited: 내가 여태까지 방문한 노드 목록
# 방문처리
visited.append(node)

# 인접 노드 방문
for adj in graph[node]:
	if adj not in visited:		    # 만약 인접한 노드(adj)가 방문한 적이 (visited) 없다면
		dfs_recursive(adj, visited) # 그 노드를 방문하자 

return visited	# 다 방문하면 visited 반환


def dfs_stack(start):			# 시작 지점 넣어줌
	visited = []			# visited는 이 때 비어있는 상태
	# 방문할 순서를 담아두는 용도로 stack 만듦, 시작 루트 붙여줌 ([start])
	stack = [start]

	# 방문할 노드가 남아있는 한 아래 로직을 반복한다.
	while stack:
		# 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
		top = stack.pop()
		visited.append(top)
		# 인접 노드를 방문한다. (= 자식이 없으면 pass)
		for adj in graph[top]:
		   if adj not in visited:
			stack.append(adj)

	return visited
