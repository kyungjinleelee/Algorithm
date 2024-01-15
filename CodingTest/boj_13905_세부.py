# 어케 해야 빼빼로를 시작점부터 끝점까지 많이 가져갈 수 있냐? (= 높은 순서대로 간선을 이어가다가, 1번 섬이랑 5번섬이 이어지는 순간을 보면 됨 )   
# 어떤 간선에 속한 최소간선가중치가 제일 최대의 가중치인지 찾는 문제 (분리집합이랑 매우 유사함 !!)

class DisjointSet:		# 분리집합 구현

    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):			          # 재귀적으로 부모 정점을 찾는 함수 
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)		      # x, y 두 노드의 부모 정점을 찾고, 
        root_y = self.find(y)
        if root_x == root_y:		      # 같으면 아무것도 안해도되고 그냥 리턴
            return
        self.parent[root_x] = root_y	# 서로 다른 부모 정점을 찾는 경우에만 두 집합을 합침


if __name__ == '__main__':
    from sys import stdin, setrecursionlimit
    input = stdin.readline
    setrecursionlimit(10 ** 5)	# 재귀 호출의 최대 깊이 지정

    n, m = map(int, input().split())		# n: 정점 갯수, m: 다리 갯수
    s, e = map(int, input().split())		# s, e: 시작 정점과 끝 정점
    bridge = []					                # bridge: 다리들의 정보를 담을 리스트 생성
    for _ in range(m):				          # 다리들 정보를 받아옴
        x, y, k = map(int, input().split())	# x, y= 정점 두개, k: 가중치
        bridge.append((k, x, y))		    # 가중치로 정렬할 것이기 때문에 가중치를 맨 앞에 넣어줌
    bridge.sort()				                # 가중치로 오름차순으로 정렬되있을 것임
    # << Disjoint Set을 활용하여 최소 가중치의 다리를 선택하면서 시작 정점과 끝 정점을 연결해주자 >>
    djs = DisjointSet(n)			          # n개의 정점으로 돌릴 DisJointSet을 하나 만들어 줌 (=초기화)
    last = 0					                  # last: 마지막으로 사용한 간선의 가중치
    while djs.find(s) != djs.find(e) and bridge: # 시작점이랑 끝점이 서로 다를 때(=연결 안됨) & bridge를 다 쓸 때까지 반복
        d, x, y = bridge.pop()			    # 가장 가중치 높은 간선을 보기 위해 맨 뒤에서 pop해줌 (d: 가중치)
        last = d				                # d를 last에 넣어줘서 갱신
        djs.union(x, y)				          # 두 개 정점을 union으로 합쳐줌
    # DisjointSet에 시작점과 끝점이 같으면(=이어졌으면) last출력, 그렇지않으면 빼빼로 0개 출력
    print(last if djs.find(s) == djs.find(e) else 0) 

"""
참고: 
Python은 재귀 함수를 최대 1500번까지 호출할 수 있음. 
이보다 많은 호출을 하려면, sys.setrecursionlimit 로 제한을 늘릴 수 있음.
"""
