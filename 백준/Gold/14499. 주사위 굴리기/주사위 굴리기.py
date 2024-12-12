# 입력 받기
N, M, x, y, K = map(int, input().split())

# 지도 정보
board = [list(map(int, input().split())) for _ in range(N)]

# 이동 명령
commands = list(map(int, input().split()))

# 주사위 초기 상태 (인덱스: [상단, 하단, 북, 남, 서, 동])
dice = [0, 0, 0, 0, 0, 0]

# 동, 서, 북, 남 방향 정의 (dx, dy)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 주사위 굴리기
def roll_dice(direction):
    top, bottom, north, south, west, east = dice
    if direction == 1:  # 동쪽
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, top
    elif direction == 2:  # 서쪽
        dice[0], dice[1], dice[4], dice[5] = east, west, top, bottom
    elif direction == 3:  # 북쪽
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif direction == 4:  # 남쪽
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top

# 이동 명령 처리
for command in commands:
    nx, ny = x + directions[command - 1][0], y + directions[command - 1][1]
    # 지도 범위 체크
    if 0 <= nx < N and 0 <= ny < M:
        # 주사위 위치 갱신
        x, y = nx, ny
        # 주사위 굴리기
        roll_dice(command)
        # 지도와 주사위 바닥면 조건에 따라 서로 복사
        if board[x][y] == 0:
            board[x][y] = dice[1]  # 주사위 바닥 -> 지도
        else:
            dice[1] = board[x][y]  # 지도 -> 주사위 바닥
            board[x][y] = 0
        # 주사위 윗면 출력
        print(dice[0])