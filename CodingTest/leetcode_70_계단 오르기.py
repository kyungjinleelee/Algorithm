# leetcode 70 계단 오르기 (Climbing Stairs)
# 재귀 써서 풀까? > 타임리밋
# DP, 피보나치수열

class Solution:
    def climbStairs(self, n):
        # 메모이제이션 배열 선언 및 초기화 (n+1: 리스트의 길이)
        stairs = [0] * (n + 1)  # 리스트의 모든 요소를 0으로 초기화
        # 첫번째 계단 오르는 경우의 수 저장
        stairs[0] = 1
        stairs[1] = 1

        # i번째 계단을 오르는 경우는 1번째 전 계단에서 오르는 경우와 2번째 전 계단에서 오르는 경우를 더한 값 (피보나치 수열)
        for i in range(2, n + 1):
            stairs[i] = stairs[i - 1] + stairs[i - 2]

        return stairs[n]
"""
stairs = [0] * (n + 1)은
n + 1은 리스트의 길이를 나타내며, 이 리스트의 모든 요소를 0으로 초기화하는 코드
 
ex)
n이 3일 경우, stairs = [0, 0, 0, 0]과 같이 초기화됨.
n이 5일 경우, stairs = [0, 0, 0, 0, 0, 0]과 같이 초기화됨.
"""
