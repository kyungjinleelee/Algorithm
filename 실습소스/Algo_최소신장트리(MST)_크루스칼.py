# 최소 신장 트리(Minimum Spanning Tree, MST)
# 주요 알고리즘 : 프림, 크루스칼
"""
크루스칼 알고리즘 작동 순서 (익숙해지면 프림보다 구현하기는 더 간단할듯 ..?)
1. 모든 간선들을 가중치에 대해 오름차순으로 정렬한다.
2. 앞에서부터, 간선을 트리에 추가했을 때, 사이클이 생기지 않는다면 그 간선을 트리에 추가한다.
   - 사이클이 생긴다면 그대로 넘어간다 (= 간선을 트리에 추가하지 않는다)
3. 2번 과정을 (전체 정점 -1)개의 간선이 트리에 추가될 때까지 반복한다.

Q. 사이클이 생겼는지 어떻게 알 수 있음? 매번 그래프 탐색을 해야 함?
A. 매 간선을 추가할 때마다 그래프 탐색을 하는 건 비효율적이라, 새로운 알고리즘을 사용해야 합니다.

==> 분리 집합 (Union-Find / Disjoint-Set) ★★
: 그래프가 유동적으로 변할 때(간선이 추가/삭제 될 때), 점들 간의 연결 여부를 빠르게 확인할 수 있어 크루스칼 알고리즘 구현 외에도 많이 사용됨
구성: 부모 정점을 찾는 `find` 함수, 서로 다른 부모 정점을 가지는 집합을 합치는 `Union` 함수
"""

# 크루스칼 알고리즘 구현
class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y	# 여기까진 분리집합


def kruskal(n, edges) -> int:
    """
    n: 정점의 개수
    edges: (정점1, 정점2, 가중치)의 리스트
    """

    # 1. 간선을 가중치 순으로 정렬
    edges.sort(key=lambda x: x[2])	# lambda함수 사용해서 정렬
    disjoint_set = DisjointSet(n)	# DisjointSet 생성
    result = 0
    used_edges = 0

    # 가중치가 낮은 간선부터 선택
    for idx, adj, cost in edges:
        # 각 노드의 부모 노드 탐색
        # 사이클이 생기지 않는다면 간선을 선택
        # 부모 노드가 같다 (두 개의 노드가 연결되어 있다) = 이 간선을 선택하면 사이클이 생긴다!
        if disjoint_set.find(idx) != disjoint_set.find(adj):	# idx와 adj를 find > 서로 다르다면 ? 
            disjoint_set.union(idx, adj)			# 합치고 (union) disjoint_set에 알려준다
            result += cost					# result에 cost 더해주고
            used_edges += 1					# 간선 한개 추가
            # 간선의 개수가 n - 1개가 되면 탐색 종료!
            if used_edges == n - 1:
                break

    return result


"""
< 분리 집합 구현 >  ★★
class DisjointSet:

    def __init__(self, n):
	# parent[idx] = idx의 부모 정점 
        self.parent = list(range(n + 1))	# 자기 자신이 대표 정점이 됨

    def find(self, x):		# 부모 정점을 찾는 함수
        if self.parent[x] == x:			# parent[x]에 갔을 때 x와 동일하면, 자신이 이미 부모정점이 되있는 거니까 그대로 x 반환
            return x
        self.parent[x] = self.find(self.parent[x]) # 'self.parent[x]'의 최신 부모 정점을 또 찾기위해 재귀함수 호출해서 갱신★★
        return self.parent[x]			# 최신 정보로 갱신
    
    def union(self, x, y):	# 서로 다른 부모 정점을 가지는 집합을 합치는 함수
        root_x = self.find(x)	# x의 부모정점, 
        root_y = self.find(y)	# y의 부모정점을 구한 다음에
        if root_x == root_y:
            return		# 같으면 아무것도 안해도되고 그냥 리턴
        self.parent[root_x] = root_y	# 다르면 self.parent[root_x]값을 root_y 값으로 갱신해줌

#예시
disjoint_set = DisjointSet(10)			  # 1~10까지 노드를 갖는 그래프
edges = [(1, 3), (2, 5), (3, 5), (4, 6), (7, 10)] # 이렇게 이어져 있는 간선들 
for idx, adj in edges:
    disjoint_set.union(idx, adj)
for i in range(1, 11):
    print(f"{i}의 부모: {disjoint_set.find(i)}")
"""


