answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    # 최대 방문 횟수 초기화
    if cnt > answer:
        answer = cnt
    
    for i in range(N):
        if k >= dungeons[i][0] and not visited[i]:
            # 방문 처리
            visited[i] = 1
            # 줄어든 피로도로 던전 방문 시작
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            # 해당 순서로 던전을 모두 방문했으니 다시 초기화
            visited[i] = 0
    
def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
