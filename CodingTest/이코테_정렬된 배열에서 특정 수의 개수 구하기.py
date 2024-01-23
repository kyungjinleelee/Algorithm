# [이코테] 정렬된 배열에서 특정 수의 개수 구하기
# 아이디어: 오른쪽 인덱스와 왼쪽 인덱스를 구하고 > 그 차이를 반환하면 됨!
"""
일반적인 for문을 활용하여 리스트를 탐색하면 시간 초과가 난다!
그렇기에 O(logN)의 시간 복잡도를 가지는 이진 탐색을 활용해야 한다.

bisect는 특정 숫자 사이에 있는 원소의 개수를 구할 때 유용하게 사용된다.
* 여기서 주의할 점은 array가 오름차순으로 sorting되어 있어야 한다는 점이다!

해당 문제의 경우 이미 오름차순으로 정렬된 수열이 input값으로 들어온다.

bisect_right(array, N)
배열에서 N이 마지막으로 등장하는 인덱스+1을 리턴함
bisect_left(array, N)
배열에서 N이 처음으로 등장하는 인덱스를 리턴함
"""
from bisect import bisect_right, bisect_left

def count_number(lst, target):
	left_idx = bisect.bisect_left(lst, target)
	if not (0 <= left_idx < len(lst) and lst[left_idx] == target):	# 왼쪽 idx가 가능한 범위 내에 있고 & target이 배열 내에 존재한다면 
		return -1	# 없다면 -1 반환
	# 있다면
	right_idx = bisect.bisect_right(lst, target)	# 우측 기준으로 한번 더 검사
	return right_idx - left_idx	# ex. target이 2일때, 6 - 2 = 4

# 테스트 코드
assert count_number(lst=[1, 1, 2, 2, 2, 2, 3], target=2) == 4
assert count_number(lst=[1, 1, 2, 2, 2, 2, 3], target=4) == -1
