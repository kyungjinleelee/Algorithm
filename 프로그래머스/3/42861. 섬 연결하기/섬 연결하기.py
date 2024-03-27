"""
- `크루스칼 알고리즘`
    - 그래프 내 모든 정점을 최소비용으로 연결함
    - 문제 中 ‘최소의 비용으로 모든 섬이 서로 통행 가능하도록’ = **최소신장트리** 구하면 댐
- 로직
    1. 모든 간선 오름차순 정렬
    2. 정렬된 순서에 맞게 그래프에 포함시킴 (중복 제거해서)
    3. 포함 시키기 전에 이미 둘이 연결 돼 있으면 무시함
"""
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2]) # 거리를 기준으로 오름차순 정렬 
    connect = set([costs[0][0]])    # 간선 연결 정보를 담는 set: 시작 연결점을 set 리스트에 추가

    # set 안에 연결된 모든 위치가 연결되기 전까지 실행
    while len(connect) != n:
        for cost in costs:
            # 이미 연결 돼 있으면 무시
            if cost[0] in connect and cost[1] in connect:
                continue
            # 두 섬 중 하나 연결 안돼있으면 비용 더하기 
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
    
    return answer
