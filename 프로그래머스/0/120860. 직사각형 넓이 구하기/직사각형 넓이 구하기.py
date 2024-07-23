def solution(dots):
    # x좌표와 y좌표를 각각 분리하여 리스트로 만듦
    x_coords = [dot[0] for dot in dots]
    y_coords = [dot[1] for dot in dots]
    
    # x축과 y축의 최소, 최대 값을 구함
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)
    
    # 직사각형의 변이 길이를 구함
    width = x_max - x_min
    height = y_max - y_min
    
    # 넓이 구하기
    return width * height