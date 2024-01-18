# 병합정렬 (mergesort)
# 구현 (합치는거)
def merge(arr1, arr2):
	result = []		# 반환할 정답 배열
	i = j = 0		# i, j를 동시에 0으로 할당 (i는 arr1, j는 arr2를 차례차례 살펴봄)
	while i < len(arr1) and j < len(arr2):
	    if arr1[i] < arr2[j]:	# i와 j를 비교, i가 작다면 i를 넣고 > i 인덱스 1 더해줌
		result.append(arr1[i])
		i += 1
	    else:
		result.append(arr2[j])	# j가 작다면 j를 넣음 > j 인덱스 1 더해줌
		j += 1

	# i든 j든 남은 녀석을 result에 통째로 붙여주자
	while i < len(arr1):
		result.append(arr1[i])
		i += 1
	
	while j < len(arr2):
		result.append(arr2[j])
		j += 1

	return result

# 구현 (쪼개는 거)
def mergesort(lst):	# mergesort 할거임. (lst 전달받기)
	if len(lst) <= 1:		# 기본적으로 길이가 1보다 같거나 작으면 
		return lst	# 주어진 배열 그대로 반환

	# 그게 아니면,
	mid = len(lst) // 2	# 중간 지점(길이를 2로 나누고 나머지 버린 정수값)을 잡는다.
	L = lst[:mid]		# 왼쪽
	R = lst[mid:]		# 오른쪽으로 나누고 

	L_sorted = mergesort(L)
	R_sorted = mergesort(R)		 # 각각 mergesort 한 다음에

	return merge(L_sorted, R_sorted) # merge로 합친 값 반환.

#  	return merge(mergesort(L), mergesort(R))	 위의 세 줄 줄이면 이케됨 

# 테스트 케이스
assert mergesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert mergesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]
