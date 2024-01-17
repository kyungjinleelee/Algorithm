"""
퀵 정렬 
분할 정복(Divide and Conquer)*을 통해 주어진 배열을 정렬하는 알고리즘.

배열에서 기준(pivot)을 잡고, 
기준보다 값이 작은 집합과 큰 집합으로 나눈다(Divide).
그리고 그 사이에 기준을 위치시킨다.

작은 집합과 큰 집합을 대상으로 재귀호출하여 정렬한 뒤(Conquer) 결과를 합치면 정렬된 배열을 얻을 수 있다. 

pivot은 보통 맨 마지막 요소로 잡는다. pivot보다 작은 집합의 인덱스 i를 -1로 설정한다. (피봇보다 작은 녀석은 없어 (i = -1)란 의미로)
"""

def quicksort(lst, start, end):
	def partition(part, ps, pe):	# part: 내가 보고있는 부분, ps: 시작 좌표, pe: 끝 좌표
		pivot = part[pe]	# 제일 마지막 녀석 피봇으로 삼음
		i = ps -1		# 시작점보다 하나 작은 녀석(-1)을 일단 i 
		for j in range(ps, pe):	# j를 통해 전 녀석을 살펴보자 (ps부터 pe-1까지)
		    if part[j] <= pivot: # 특정 녀석(j)이 피봇보다 작다면?
			i += 1		# i보다 작은 집합의 칸을 하나 늘려줌 (+1)
			part[i], part[j] = part[j], part[i]	# 그 자리에 지금 내가 보고있는 녀석(j)를 넣어줌
		# 작지 않다면
		part[i + 1], part[pe] = part[pe], part[i + 1]	# i보다 한 칸 늘리고, 마지막 피봇의 위치(pe)와 바꿔줌 
		return i + 1
	
	if len(lst) == 1:
		return lst

	if start >= end:	# 종료 조건 (partition 더 이상 실행하지마)
		return None

	p = partition(lst, start, end)	# partition이 lst 전체를 보고, start, end
	quicksort(lst, start, p - 1)	# 재귀적으로 quicksort 호출 
	quicksort(lst, p + 1, end)
	return lst

# 테스트 코드 
assert quicksort([4, 6, 2, 9, 1], 0, 1) == [4, 6, 2, 9, 1]	# 0부터 1까지만 정렬
assert quicksort([4, 6, 2, 9, 1], 0, 2) == [2, 4, 6, 9, 1]	# 0부터 2까지만 정렬
assert quicksort([4, 6, 2, 9, 1], 0, 3) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 4) == [1, 2, 4, 6, 9]	# 전부 다 정렬 (start: 0, end: 4, lst: [4, 6, 2, 9, 1]이 됨)

# 재귀는 종료지점을 잘 설정하는게 중요함 
