t = int(input())  # 톱니바퀴의 갯수
# 톱니바퀴 상태
condition = [list(input().strip()) for _ in range(t)]
# print(condition) # [['10101111'], ['01111101'], ['11001110'], ['00000010']]
k = int(input())  # 회전 횟수
# 회전 시킬 방법
way = [list(map(int, input().split())) for _ in range(k)]
# print(way)  # [['3', '-1'], ['1', '1']] -> [[3, -1], [1, 1]] (문자열로 작업하면 슬라이싱 결과를 새로 저장하기 어려움)


# 시계 방향 회전 함수
def rotate(data):
    return data[-1:] + data[:-1]  # 마지막 요소를 앞으로 이동

# 반시계 방향 회전 함수
def reverse_rotate(data):
    return data[1:] + data[:1]  # 첫 번째 요소를 뒤로 이동

# 연쇄 회전을 처리하는 함수
def rotate_gears(gear_index, direction):
    visited = [False] * t  # 이미 회전한 톱니바퀴를 추적
    rotations = [(gear_index, direction)]  # 회전해야 할 톱니바퀴와 방향을 저장

    # 회전 연쇄 처리
    while rotations:
        current_index, current_direction = rotations.pop(0)
        if visited[current_index]:
            continue
        visited[current_index] = True

        # 왼쪽 톱니바퀴 검사
        if current_index > 0 and not visited[current_index - 1]:
            if condition[current_index][6] != condition[current_index - 1][2]:
                rotations.append((current_index - 1, -current_direction))

        # 오른쪽 톱니바퀴 검사
        if current_index < t - 1 and not visited[current_index + 1]:
            if condition[current_index][2] != condition[current_index + 1][6]:
                rotations.append((current_index + 1, -current_direction))

        # 현재 톱니바퀴 회전
        if current_direction == 1:  # 시계 방향
            condition[current_index] = rotate(condition[current_index])
        elif current_direction == -1:  # 반시계 방향
            condition[current_index] = reverse_rotate(condition[current_index])


# 회전 명령 처리
for num, direction in way:
    rotate_gears(num - 1, direction)  # 번호는 1부터 시작하므로 인덱스는 num - 1

# 12시 방향이 S극인 톱니바퀴의 개수 출력
answer = 0
for gear in condition:
    if gear[0] == '1':
        answer += 1
print(answer)