def solution(sizes):
    max_width = 0
    max_height = 0
    
    # 각 명함의 가로, 세로 중 큰 값을 가로로, 작은 값을 세로로 설정
    for size in sizes:
        width, height = sorted(size, reverse = True)
        max_width = max(max_width, width)
        max_height = max(max_height, height)
    
    # 최종적으로 가장 큰 가로 길이 * 세로 길이
    return max_width * max_height