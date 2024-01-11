# dfs (재귀)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []                           # 빈 리스트로 초기화, 모든 부분집합이 저장

        def dfs(index, path):                 # 재귀적으로 부분집합 형성하는 함수. index: 현재 탐색 중인 요소의 인덱스, path: 현재까지의 부분집합
            answer.append(path)               # 현재 부분집합 path를 answer 리스트에 추가

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)): # 현재 인덱스부터 nums 배열의 끝까지 반복 
		            # dfs함수 재귀적 호출
                dfs(i + 1, path + [nums[i]])  # i+1: 인덱스 업데이트, path+[nums[i]]: 현재까지의 부분집합에 현재요소 추가하여 새로운 부분집합 생성 

        dfs(0, [])                            # 초기인덱스 0과 빈[]로 dfs 호출 (초기화)
        return answer


"""
이 부분은 현재 요소를 선택한 경우와 선택하지 않은 경우 두 가지 상황을 고려하여 모든 가능한 부분집합을 생성함. 재귀 호출을 통해 모든 경우의 수를 다루고, 이를 통해 전체 부분집합을 구할 수 있음.

예시: nums = [1, 2, 3]의 경우, dfs(0, [])이 처음 호출되면 다음과 같은 재귀 호출이 발생함:

dfs(1, [1]): 1을 선택한 경우
dfs(2, [1, 2]): 2를 선택한 경우
dfs(3, [1, 2, 3]): 3을 선택한 경우
이런 식으로 모든 경우의 수를 고려하여 부분집합을 생성하게 됨.
"""
