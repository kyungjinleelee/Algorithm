class DisjointSet:

    def __init__(self, n):
	# parent[idx] = idx의 부모 정점 
        self.parent = list(range(n + 1))	          # 자기 자신이 대표 정점이 됨

    def find(self, x):		# 부모 정점을 찾는 함수
        if self.parent[x] == x:			               # parent[x]에 갔을 때 x와 동일하면, 자신이 이미 부모정점이 되있는 거니까 그대로 x 반환
            return x
        self.parent[x] = self.find(self.parent[x]) # 'self.parent[x]'의 최신 부모 정점을 또 찾기위해 재귀함수 호출해서 갱신★★
        return self.parent[x]			                  # 최신 정보로 갱신
    
    def union(self, x, y):	        # 서로 다른 부모 정점을 가지는 집합을 합치는 함수
        root_x = self.find(x)	      # x의 부모정점, 
        root_y = self.find(y)	      # y의 부모정점을 구한 다음에
        if root_x == root_y:
            return		              # 같으면 아무것도 안해도되고 그냥 리턴
        self.parent[root_x] = root_y	# 다르면 self.parent[root_x]값을 root_y 값으로 갱신해줌

#예시
disjoint_set = DisjointSet(10)			              # 1~10까지 노드를 갖는 그래프 생성 
edges = [(1, 3), (2, 5), (3, 5), (4, 6), (7, 10)] # 이렇게 이어져 있는 간선들 
for idx, adj in edges:			                      # edges 리스트에 있는 간선들을 하나씩 꺼냄 ( 각 간선은 정점 idx, adj로 이뤄져있음 )
    disjoint_set.union(idx, adj)		              # union 메서드 통해 집합 합침
for i in range(1, 11):				                    # 1~10까지의 각 노드에 대해 
    print(f"{i}의 부모: {disjoint_set.find(i)}")	  # 부모를 찾아서 출력함

"""
출력 결과:
1의 부모: 3
2의 부모: 5
3의 부모: 3
4의 부모: 6
5의 부모: 5
6의 부모: 6
7의 부모: 10
8의 부모: 8
9의 부모: 9
10의 부모: 10

해석:
1과 3이 같은 집합에 속하고 있음을 나타냅니다.
2와 5가 같은 집합에 속하고 있음을 나타냅니다.
3은 이미 부모 정점이 자기 자신이 아니기 때문에 최신 정보로 갱신되었습니다.
4와 6이 같은 집합에 속하고 있음을 나타냅니다.
7과 10이 같은 집합에 속하고 있음을 나타냅니다.
8, 9, 10은 각각 자기 자신이 부모 정점이 되어 있는 독립적인 집합입니다.
"""
