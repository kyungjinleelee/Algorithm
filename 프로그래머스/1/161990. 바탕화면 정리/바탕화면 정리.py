def solution(wallpaper):
    # 파일 위치 초기화
    min_row, min_col = 51, 51
    max_row, max_col = -1, -1
    
    # 파일 위치 탐색
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)
                
    # 드래그 시작점과 끝점 계산
    lux, luy = min_row, min_col
    rdx, rdy = max_row + 1, max_col + 1
    
    return [lux, luy, rdx, rdy]