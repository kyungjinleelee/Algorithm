def solution(box, n):
    # 가로 방향으로 들어갈 수 있는 정육면체 개수
    x = box[0] // n
    # 세로 방향으로 들어갈 수 있는 정육면체 개수
    y = box[1] // n
    # 높이 방향으로 들어갈 수 있는 정육면체 개수
    z = box[2] // n
    
    return x * y * z