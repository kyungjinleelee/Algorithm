# leetcode 704 Binary Search (이분탐색)
# 구현해서 풀 수도 있고 내장된 라이브러리 써서 풀 수도 있음
# 구현해서 풀기
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(start, end):
            if start > end:
                return -1   # 시작점이 끝점보다 큰 건 말이 안돼서 -1 리턴

            mid = (start + end) // 2

            if nums[mid] < target:      # 원하는 값(target)보다 작다면,
                return bs(mid + 1, end) # 중간값 +1에서 끝까지 다시 이분탐색
            elif nums[mid] > target:    # target보다 크다면
                return bs(start, mid - 1)   # 처음부터 중간값 -1까지 다시 이분탐색
            else:           # 둘 다 아니라면 target임
                return mid
        return bs(0, len(nums) - 1)
        
# 내장된 걸로 풀기
class Solution:
    import bisect
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)		# bisect라는 라이브러리..! 내가 찾는 값 (nums, target) 그대로 넘겨주면 됨
        if idx < len(nums) and nums[idx] == target:	# 결과값(idx)이 nums길이보다 짧고, idx는 target의 nums에 있는 인덱스라면
            return idx					# 그대로 리턴
        else:
            return -1
          
"""
# target이 있는 경우에는, target의 제일 왼쪽 인덱스 값 반환! 없는 경우에는, target보다 작은 요소들보다 하나 큰 인덱스값을 줌
def binary_search_builtin(nums, target):
	# [-1, 1, 2, 2, 2, 3] 2
	# bisect_left -> 2

	# [-1, 1, 3, 3, 5] 2  / bisect_left -> 2 
	# [-5, -4, -4, -2, -1] 2 (전부 2보다 작다면, 전체 길이인 5 반환)
	# [3, 4, 5, 6, 7] 2 (0 반환, 전부 다 2보다 크기 때문)

	idx = bisect.bisect_left(nums, target)	
	if idx < len(nums) and nums[idx] == target:	
		return idx				
	else:
		return -1
"""
