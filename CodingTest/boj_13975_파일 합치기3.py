# boj 13975 파일 합치기 3
# 그리디 알고리즘
# 소설의 각 장들이 수록되어 있는 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 문제
# 40 30 30 50 이 입력받는다고 가정했을 때, 파일크기가 50인 파일은 합쳐지는 시기를 최대한 뒤로 빼야만 함. 즉, 작은 애들을 최대한 앞에 둬야함.

from sys import stdin
from heapq import heapify, heappop, heappush

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    files = list(map(int, input().split()))	# 파일의 크기를 저장할 리스트 받아옴
    heapify(files)		# 힙 구조를 써야하기 때문에 heapify 해줌 (최소힙구조)
    ans = 0
    for _ in range(n - 1):	# 파일의 갯수가 4개면, 3번 합쳐야되니까 n - 1번 반복
        a = heappop(files)	# 최소크기 파일 두 개(a, b)를 뽑아(heappop)온 다음,
        b = heappop(files)
        ans += a + b		# 두 개를 합친 크기만큼 ans에 갱신 
        heappush(files, a + b)	# 합친 걸 새로운 files 더미에 추가(push)한다.
    print(ans)			# ans = 모든 파일을 합칠 때의 최소 비용이 누적되어 반환

"""
힙을 사용한 이유
- 각 단계에서 항상 가장 작은 두 파일을 뽑아와야 하는데, 최소 힙 구조를 사용하면 항상 가장 작은 값에 빠르게 접근할 수 있음
- 힙은 우선순위 큐를 구현하는데에 효과적이며, 가장 작은 값을 효율적으로 찾을 수 있기 때문

- Heap을 사용하지 않고 리스트 등의 자료구조를 사용할 경우, 각 단계에서 가장 작은 값 찾기 및 삭제, 새로운 값 추가에 대한 연산이 O(n)의 시간이 걸릴 수 있음.
- 그러나 최소 힙을 사용하면 이러한 연산이 O(log n)으로 빠르게 수행됨. 
- 따라서 Heap을 사용하면 알고리즘의 성능을 향상시킬 수 있음.
"""
