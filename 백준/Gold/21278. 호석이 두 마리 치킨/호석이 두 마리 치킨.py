from itertools import combinations

N, M = map(int, input().split())
edges = [input().strip() for _ in range(M)]
# print(edges) # ['1 3', '4 2', '2 5', '3 2']

INF = float('inf')

# 그래프 초기화
dist = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    # 자기 자신까지의 거리는 0
    dist[i][i] = 0

for edge in edges:
    A, B = map(int, edge.split())
    dist[A][B] = 1  # 도로의 거리는 항상 1
    dist[B][A] = 1  # 양방향

# 플로이드-워셜
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 치킨집 위치 선정
best_pair = None
min_total_distance = INF

for chicken1, chicken2 in combinations(range(1, N + 1), 2):
    total_distance = 0

    for building in range(1, N + 1):
        # 가장 가까운 치킨집까지의 왕복 거리 계산
        closest_distance = min(dist[building][chicken1], dist[building][chicken2])
        total_distance += closest_distance * 2  # 왕복 거리

    # 최적의 조합 업데이트
    if total_distance < min_total_distance:
        min_total_distance = total_distance
        best_pair = (chicken1, chicken2)
    elif total_distance == min_total_distance:
        if (chicken1, chicken2) < best_pair:
            best_pair = (chicken1, chicken2)

print(best_pair[0], best_pair[1], min_total_distance)
