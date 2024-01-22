# leetcode 349 두 배열의 교집합 Intersection of Two Arrays
# 이진탐색으로 풀음
import bisect

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        result = set()  # 중복 어차피 걸러줄거니까 다 때려넣고 > list(result)로 반환하자. -> 아이디어
        nums2.sort()    # 두 배열 중 한 배열 sort

        for n1 in nums1:    # 나머지 한 배열의 요소를 꾸준히 찾으며 num2에서 이분탐색 하겠다 !
            idx = bisect.bisect_left(nums2, n1) # idx: n1이 들어갈 위치의 인덱스가 저장
            if len(nums2) > idx and n1 == nums2[idx]:   # idx가 nums2의 길이를 초과하지 않는지 확인 & n1이 nums2 배열에서 찾아졌는지 확인
                result.add(n1)  # true이면 result에 n1 추가

        return list(result)
        

"""
- set()의 특징 -
set()은 파이썬에서 내장된 데이터 타입 중 하나로, 집합(Set)을 나타낸다. 
Set의 특징:
중복된 요소가 없음: Set은 중복된 값을 허용하지 않는다. 동일한 값을 여러 번 추가하더라도 한 번만 저장된다.
순서가 없음: Set은 순서가 없는 데이터 구조이기 때문에 인덱스를 사용하여 원소에 접근할 수 없다.
가변성(Mutable): Set은 가변적인 데이터 타입이며, 원소를 추가하거나 제거할 수 있다.
"""
""" 
- 이진탐색이 중요한 이유 -
이중for문 돌려서 풀어도 된다. 이 문제의 경우 1000*1000이라 그렇게까지 부담되는 연산은 아니지만, 10000*10000만 돼도 시간초과가 날 수 있음.
"""
