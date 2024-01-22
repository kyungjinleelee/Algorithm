# leetcode 53 최대 서브 배열 Maximum Subarray
"""
입력 값으로는 nums라는 배열이 들어오고, 배열 안에는 최소 하나의 정수가 존재한다.
배열 원소들 중 연속되는 subarray의 합이 최대가 되는 것을 찾아 return 하는 문제.
"""
# 방법 1. 이중 For문으로 노가다하기 -시간 복잡도 O(N^2) - 느려서 Time Limit Exceeded 에러 발생함
# 가능한 부분 배열들을 모두 살펴본 후 합을 구해서 가장 큰 값을 찾는 방식
# Brute-Force Approach
# Output Limit Exceeded
class Solution:
    def maxSubArray(self, nums):
        max_sum = -inf			# 초기값은 음의 무한대(-inf)로 설정
        for i in range(len(nums)):	
            cur_sum = 0			# cur_sum: 현재 부분 배열의 합
            for j in range(i, len(nums)):
                print(nums[i:j])
                cur_sum += nums[j]
                max_sum = max(cur_sum, max_sum)	# cur_sum과 max_sum 중에서 더 큰 값을 max_sum에 갱신
        return max_sum

# 방법 2. 다이나믹 프로그래밍으로 풀기 , 시간 복잡도 O(N)
# 이전 계산된 부분합을 사용하기 때문에 모든 부분합을 처음부터 다시 계산하지 않는다.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current_subarray: 현재까지의 부분 배열 합, max_subarray: 최대 연속 부분 배열의 합
        # 두 변수를 입력 리스트의 첫 번째 원소로 초기화
        current_subarray = max_subarray = nums[0]
        
        # nums에서 두 번째 원소부터 마지막 원소까지 순회 (첫 번째 원소는 이미 초기화 단계에서 고려함)
        for num in nums[1:]:
            # 만약 current_subarray가 음수가 되면 현재 원소만으로 새로운 부분 배열 시작
            # 그렇지 않으면 현재 원소를 이전 부분 배열에 추가 (current_subarray + num)
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)  # 갱신
        
        return max_subarray
