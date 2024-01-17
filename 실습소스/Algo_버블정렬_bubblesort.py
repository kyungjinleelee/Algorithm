"""
버블 정렬 (정렬 중에 젤 쉬움!)
첫 번째 자료와 두번째 자료를, 두 번째 자료와 세 번째 자료를, 세 번째와 네 번째를, ... 이런 식으로 
(마지막-1)번째 자료와 마지막 자료를 비교해서 교환하면서 자료를 정렬하는 방식

작은 숫자, 큰 숫자 순서로 있으면 내버려두고 
큰 숫자, 작은 숫자 순서로 있으면 둘의 위치 변경하면 댐
"""

def bubblesort(lst):
	# 최댓값을 구하는 알고리즘을 len(lst) -1 만큼 반복한다.
	iters = len(lst) - 1		# 전체 반복 횟수 = 전체 갯수 - 1
	for iter in range(iters):	# 반복 횟수
		# 이미 구한 최댓값은 범위에서 제외한다.
		wall = iters - iter	# 전체 반복 횟수 - 반복 갯수
		for cur in range(wall):	# 나의 위치는(cur) 0에서부터 wall 만큼 반복
		     if lst[cur] > lst[cur + 1]:				# 지금 위치가 더 크다면
			   lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]	# 둘의 위치 바꾸셈
	return lst

"""
디버거 모드로 이해해보자..
def bubblesort(lst):				lst: [4, 6, 2, 9, 1]
	iters = len(lst) - 1			iters: 4
	for iter in range(iters):		iter: 0 (iter는 0에서부터 3까지)
		wall = iters - iter		wall: 4
		for cur in range(wall):		cur: 0  (cur는 0에서부터 3까지 이동)
		     # 0) 0, 1 비교 (4, 6 순차적으로 되있음) 			[4, 6, 2, 9, 1] 
		     # 1) 1, 2 비교 (6, 2 순차적 x, if문에 해당됨 > 둘 사이 자리 바꿔줌) [4, 2, 6, 9, 1]
		     # 2) 2, 3 비교 (6, 9 순차적으로 되있음)			  [4, 2, 6, 9, 1]
		     # 3) 3, 4 비교 (9, 1 순차적 x, if문에 해당됨 > 둘 사이 자리 바꿔줌) [4, 2, 6, 1, 9]
		     # cur: 3이기 때문에 한 바퀴 돌기 완료 !!! 
		     # 1) iters: 4, iter: 1, wall: 3에서부터 다시 시작 ..
		     if lst[cur] > lst[cur + 1]: 				
			   lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]	
	return lst
"""

# 테스트 코드
assert bubblesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
