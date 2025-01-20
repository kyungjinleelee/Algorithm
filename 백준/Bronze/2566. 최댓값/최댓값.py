# 9x9 행렬 입력 받기
matrix = [list(map(int, input().split())) for _ in range(9)]

# 최댓값과 위치 초기화
max_value = -1
max_row, max_col = -1, -1

# 행렬 순회
for i in range(9):  # 행 인덱스
    for j in range(9):  # 열 인덱스
        if matrix[i][j] > max_value:  # 최댓값 갱신
            max_value = matrix[i][j]
            max_row, max_col = i + 1, j + 1  # 행, 열은 1부터 시작

# 결과 출력
print(max_value)
print(max_row, max_col)