def solution(nums):
    unique_types = len(set(nums))   # 고유 종류 갯수
    picks = len(nums) // 2          # 선택할 수 있는 개수 (N/2)
    return min(unique_types, picks)