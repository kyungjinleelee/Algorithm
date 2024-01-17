"""
선택 정렬 
말 그대로 '선택! 해서 정렬한다' 라고 이해하면 됨.
버블 정렬보다 훨씬 더 적은 비교를 하는 것 같지만, 실제론 각 배열을 계속해서 탐색하는 방식이라 2중 반복문을 사용해야 함
"""
def selectionsort(lst):
	iters = len(lst) - 1
	for iter in range(iters):
		mininum = iter		# 일단 제일 작은 값(minimum)이 앞에 있는 녀석(iter)이라고 가정하자.
		for cur in range(iter + 1, len(lst):
		    if lst[cur] < lst[minimum]:	# 지금 현재 값이 더 작으면
			minimun = cur		# 최솟값을 현재 값(cur)으로 해줌

		if minimum != iter:	# 최솟값과 앞에 있는 녀석의 위치가 다르면, 
		    lst[minimum], lst[iter] = lst[iter], lst[minimun]	# 자리 바꿔주자


# 테스트 코드
assert selectionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
