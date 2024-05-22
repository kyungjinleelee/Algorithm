def solution(board, k):
    total = 0
    rows = len(board)
    cols = len(board[0])
    
    for i in range(rows):
        for j in range(cols):
            if i + j <= k:
                total += board[i][j]
    return total