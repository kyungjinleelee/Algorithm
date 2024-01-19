# m x m 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하는 문제
# 행렬의 세로와 가로는 모두 정렬되어 있음
""" 
아이디어 :
문제가 왼쪽 -> 오른쪽, 위 -> 아래쪽으로 정렬되어 있으므로 맨 오른쪽 위에서 시작하면 target보다 작을 때와 클 때 모두 반응할 수 있다.
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix: 행렬, target: 목표값
        if not matrix: # matrix 비어있으면
            return False

        row = 0
        col = len(matrix[0]) - 1    # matrix의 첫번째 행의 열의 갯수 -1 (= 행렬의 오른쪽 맨 위에서 시작)

        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if matrix[row][col] == target:  # 현재 위치의 값 == target이면
                return True
            elif matrix[row][col] < target: # 목표값보다 작으면
                row += 1                    # 그 다음 행으로 이동
            else:           # 목표값보다 크면
                col -= 1    # 현재 열을 왼쪽으로 이동 
        # while 루프 벗어난다 = 행렬 범위 벗어난다 = 목표값이 행렬 안에 없다 
        return False
