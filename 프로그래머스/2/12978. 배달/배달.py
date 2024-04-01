import heapq

INF = 10000*50
                
def solution(N, road, K):
    dist = [INF] * (N+1)
    dist[1] = 0
    
    graph = [[] for _ in range(N+1)]
    
    for route in road:
        start, end, edge = route
        graph[start].append((end, edge))
        graph[end].append((start, edge))
        
    heap = []
    heapq.heappush(heap, (0, 1))
    
    while heap:
        dis, cur = heapq.heappop(heap)
        if dist[cur] < dis:
            continue
        for node in graph[cur]:
            if node[1] + dis < dist[node[0]]:
                dist[node[0]] = node[1] + dis
                heapq.heappush(heap, (dist[node[0]], node[0]))
                
    answer = 0
    for i in dist:
        if i <= K:
            answer += 1

    return answer