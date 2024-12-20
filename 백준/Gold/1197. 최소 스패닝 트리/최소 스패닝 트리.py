# 크루스칼 알고리즘 구현
def find(parent, x):
    """유니온-파인드: 루트 노드 찾기"""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    """유니온-파인드: 두 집합 합치기"""
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

def kruskal(v, edges):
    """크루스칼 알고리즘"""
    # 간선을 가중치 기준 오름차순 정렬
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(v + 1)] # 부모 초기화
    rank = [0] * (v + 1) # 랭크 초기화

    total_weight = 0
    for a, b, weight in edges:
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            total_weight += weight
    return total_weight

# 입력
v, e = map(int, input().split())
edges = []

for i in range(1, e + 1):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 최소 스패닝 트리의 가중치 계산
result = kruskal(v, edges)
print(result)
