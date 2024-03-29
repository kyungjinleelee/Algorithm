def dfs(n, computers, com, visited):
    visited[com] = True # 방문하면 True로 방문 표시 
    for connect in range(n):
        # 현재 노드와 연결되어있고, 자기 자신이 아닌 경우
        if connect != com and computers[com][connect] == 1:
            # 방문하지 않은 노드에 대해서 dfs 재귀 호출 
            if visited[connect] == False:
                dfs(n, computers, connect, visited)


def solution(n, computers):                     # 노드수, 연결정보
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):                        # 모든 노드(컴퓨터) 살펴보기
        if visited[com] == False:               # 그 노드가 어느 것과 연결되어 있지 않다면
            dfs(n, computers, com, visited)     # 그 노드와 직, 간접적으로 연결되어 있는 것을 DFS로 찾기
            answer += 1                         # 연결 돼있는 노드 방문끝나면 + 1
    return answer
