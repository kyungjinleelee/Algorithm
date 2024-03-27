def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2]) # 거리를 기준으로 오름차순 정렬 
    connect = set([costs[0][0]])    # 간선 연결 정보를 담는 set
    
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