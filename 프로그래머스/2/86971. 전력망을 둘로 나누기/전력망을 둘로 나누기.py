from collections import deque
import sys

# bfs탐색을 통해 현재 연결된 그래프들의 개수를 구한다.
def bfs(start, visited, arr):
    cnt = 1
    q = deque()
    q.append(start)
    
    while q:
        cnt += 1
        v = q.popleft()
        
        for nv in arr[v]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
    
    return cnt

def solution(n, wires):
    answer = sys.maxsize
    
    # 인접 리스트 만들기
    arr = [[] for _ in range(n + 1)]
    for wire in wires:
        node_1, node_2 = wire[0], wire[1]
        arr[node_1].append(node_2)
        arr[node_2].append(node_1)
    
    # 모든 간선을 하나씩 없애보면서, 송전탑 개수 차이를 갱신한다.
    for wire in wires:
        node_1, node_2 = wire[0], wire[1]
        
        # 두 간선 끝점을 방문처리한다
        visited = [None] + [False] * n
        visited[node_1] = True
        visited[node_2] = True
        
        # 예제1 기준 : #4번노드, #7번노드로부터 연결된 노드 개수를 구한다.
        # 6개, 3개
        cnt_1 = bfs(node_1, visited, arr)
        cnt_2 = bfs(node_2, visited, arr)
        
        # 송전탑 개수 차이 갱신
        answer = min(answer, abs(cnt_1 - cnt_2))
        
    return answer