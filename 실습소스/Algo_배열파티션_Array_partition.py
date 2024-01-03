from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #입력받는 리스트 오름차순으로 정렬 후, 합계를 0으로 초기화
        nums.sort()
        sum = 0 

        #입력받은 리스트를 반복하면서 짝수번째 인덱스값을 sum에 더함
        for i in range(0, len(nums), 2):
            sum += nums[i]

        return sum

        #위의 다섯 줄을, 슬라이싱을 이용해 한 줄로 줄일 수 있음(n번씩 건너뛰는 방식)
        # return sum(sorted(nums)[::2])
