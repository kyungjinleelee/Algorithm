# 문제: https://www.acmicpc.net/problem/1922
#  최소신장트리를 구해서 그 최소신장트리에 구성된 간선들의 가중치의 합을 구하면 되는 문제 
# 변형없는 전형적인 최소신장트리 문제임
# 최소신장트리 문제는 구현보다 문제를 보고 아, MST 써야겠다하고 아는게 더 중요함
# Q. 그럼 어떻게 알아야 하나여?
# A.문제 내에 '비용을 최소로 한다'와 같은 워딩ㅇ..을 보고 알 수 잇다

def prim(n, edges):
    import heapq
    
    graph = [[] for _ in range(n + 1)]
    for idx, adj, cost in edges:    # idx: 정점1, adj: 정점2, cost: 가중치
        graph[idx].append((cost, adj))
        graph[adj].append((cost, idx))
        
    # 1. 임의의 정점을 시작으로 선택한다.
    visited = [False] * (n + 1)
    visited[1] = True
    heap = []
    for cost, adj in graph[1]:
        heapq.heappush(heap, (cost, adj)) # 2. 해당 정점과 연결된 간선을 탐색 대상에 추가해줌
    
    result = 0
    used_edges = 0
    while used_edges < n - 1:
        # 3. 가중치 낮은 간선을 선택한다.
        cost, idx = heapq.heappop(heap)
        # idx가 이미 방문한 정점이라면 패스 
        if visited[idx]:
            continue
        # 방문하지 않은 경우
        visited[idx] = True
        result += cost
        used_edges += 1
        # 4. 선택한 정점과 연결된 간선을 우선순위 큐에 넣는다. 
        for adj_cost, adj in graph[idx]:
            if not visited[adj]:
                heapq.heappush(heap, (adj_cost, adj))
                
    return result    # result에 누적된 최소신장트리의 가중치 반환


if __name__ == '__main__':
    from sys import stdin
    input = stdin.readline
    n = int(input())
    m = int(input())		# n(정점의 갯수), m(간선의 갯수) 받아오고 
    edges = [tuple(map(int, input().split())) for _ in range(m)]    # m개의 줄에 걸쳐서 간선들의 정보를 입력받음
    print(prim(n, edges))	# 구현한 최소신장트리 알고리즘에 대입 하고 > 출력! 끝!
