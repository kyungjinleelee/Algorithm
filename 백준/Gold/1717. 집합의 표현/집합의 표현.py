def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]


def union(parent, size, a, b):
    root_a = find(parent, a)  # a가 속한 집합의 루트 노드 찾기
    root_b = find(parent, b)  # b가 속한 집합의 루트 노드 찾기

    # 루트가 다를 때만 합집합 수행
    if root_a != root_b:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a
        size[root_a] += size[root_b]  # 크기 갱신

def initialize(n):
    parent = list(range(n + 1))  # 각 노드는 자기 자신이 부모
    size = [1] * (n + 1)  # 각 집합의 초기 크기는 1
    return parent, size

def solution():
    n, m = map(int, input().split())
    parent, size = initialize(n)

    result = []
    for _ in range(m):
        op, a, b = map(int, input().split())
        if op == 0: # 합집합 연산
            union(parent, size, a, b)
        elif op == 1: # 같은 집합 여부 확인
            if find(parent, a) == find(parent, b):
                result.append("YES")
            else:
                result.append("NO")
    print(*result, sep="\n")

solution()