def solution(n):
    # 배열 초기화
    answer = [[0] * n for _ in range(n)]
    
    # 초기 설정
    num = 1
    top, bottom, left, right = 0, n-1, 0, n-1
    
    while top <= bottom and left <= right:
        # 왼쪽 -> 오른쪽
        for i in range(left, right + 1):
            answer[top][i] = num
            num += 1
        top += 1
        
        # 위 -> 아래
        for i in range(top, bottom + 1):
            answer[i][right] = num
            num += 1
        right -= 1
        
        # 오른쪽 -> 왼쪽
        for i in range(right, left -1, -1):
            answer[bottom][i] = num
            num += 1
        bottom -= 1
        
        # 아래 -> 위
        for i in range(bottom, top -1, -1):
            answer[i][left] = num
            num += 1
        left += 1
    
    return answer