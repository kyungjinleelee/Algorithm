from collections import Counter

def solution(nums):
    answer = Counter(nums)
    if len(list(answer.values())) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(list(answer.values()))