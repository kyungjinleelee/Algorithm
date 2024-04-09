answer = 0
N = 0
visited = []

# dfs 재귀 호출
def dfs(k, cnt, dungeons): # cnt: 현재까지 방문한 던전의 수
    global answer
    # 최대 방문 횟수 초기화
    if cnt > answer:
        answer = cnt
    
    for i in range(N):
        # 현재 피로도(k)가 던전의 피로도보다 크고, 방문 안됐을 경우에만 탐색 진행 
        if k >= dungeons[i][0] and not visited[i]:
            # 방문 처리
            visited[i] = 1
            # 피로도 줄이고 다음 던전 방문, 방문 횟수 +1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            # 해당 순서로 던전을 모두 방문했으니 다시 초기화
            visited[i] = 0
    
def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
