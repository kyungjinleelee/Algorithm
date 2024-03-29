from collections import deque

def bfs(n, computers, com, visited):
    visited[com] = True
    Q = deque()
    Q.append(com)
    while Q:
        com = Q.popleft()
        visited[com] = True 
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    Q.append(connect)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):                        # 모든 노드(컴퓨터) 살펴보기
        if visited[com] == False:               # 그 노드가 어느것과 연결되어 있지 않다면
            bfs(n, computers, com, visited)     # 그 노드와 직, 간접적으로 연결 돼 있는 것을 BFS로 찾기
            answer += 1
    return answer
