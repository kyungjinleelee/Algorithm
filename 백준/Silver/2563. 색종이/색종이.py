n = int(input())
canvas = [[0] * 100 for _ in range(100)] # 100 * 100 크기의 도화지 (2차원 배열)

# 색종이 붙이기
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10): # 색종이의 가로 범위
        for j in range(y, y + 10): # 색종이의 세로 범위
            canvas[i][j] = 1 # 해당 영역을 검은색(1)으로 채움

# 검은 영역 넓이 계산
black_area = sum(row.count(1) for row in canvas)
print(black_area)