n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_repaints(x, y):
    repaint_w = 0  # 왼쪽 위가 'W'인 경우
    repaint_b = 0  # 왼쪽 위가 'B'인 경우

    for i in range(8):
        for j in range(8):
            # (i+j) % 2가 0이면 시작 색깔, 1이면 반대 색깔
            if (i + j) % 2 == 0:
                if board[x + i][y + j] != 'W':  
                    repaint_w += 1  
                if board[x + i][y + j] != 'B':  
                    repaint_b += 1  
            else:
                if board[x + i][y + j] != 'B':  
                    repaint_w += 1  
                if board[x + i][y + j] != 'W':  
                    repaint_b += 1  
    
    return min(repaint_w, repaint_b)

min_repaint = float('inf')

# 가능한 모든 8x8 부분 보드 탐색
for i in range(n - 7):
    for j in range(m - 7):
        min_repaint = min(min_repaint, count_repaints(i, j))

print(min_repaint)