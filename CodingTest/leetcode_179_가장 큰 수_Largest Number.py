"""
주어진 비음수 정수 리스트 nums가 주어지면, nums를 가장 큰 수를 형성하도록 배열하는 문제.
조건: 결과가 매우 큰 수일 수 있기 때문에 정수 대신 문자열로 반환해야 함 
"""

class Solution:

    @staticmethod   # 이 함수를 class내의 method로 취급하지 않겠다.는 뜻
    def to_swap(A: int, B: int) -> bool:           # ex) A=3, B=30일 때
        return str(A) + str(B) < str(B) + str(A)   # 330이 큼 303이 큼? 

    def largestNumber(self, nums: List[int]) -> str:
        
        #삽입정렬 코드
        for i in range(len(nums)):
            for j in range(i, 0, -1):       # j는 i에서부터 시작해서 이전 위치로 거슬러 올라가면서 비교 
                if(self.to_swap(nums[j-1], nums[j])): # nums[j]와 nums[j-1] 비교
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                
        return str(int(''.join(map(str, nums))))    # 문자열로 바꿔서 반환
