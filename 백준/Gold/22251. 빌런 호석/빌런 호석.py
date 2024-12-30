# 반전 : 켜진 부분은 끄고, 꺼진 부분은 켜는 것
n, k, p, x = map(int, input().split())

# 숫자를 LED 상태로 표현한 비트마스크
LED_STATE = [
    0b1110111,  # 0
    0b0010010,  # 1
    0b1011101,  # 2
    0b1011011,  # 3
    0b0111010,  # 4
    0b1101011,  # 5
    0b1101111,  # 6
    0b1010010,  # 7
    0b1111111,  # 8
    0b1111011   # 9
]

def count_led_changes(x, y):
    """x를 y로 변환할 때 필요한 LED 반전 개수"""
    return bin(LED_STATE[x] ^ LED_STATE[y]).count('1')

def solve(n, k, p, x):
    x_str = str(x).zfill(k)  # 현재 층수
    result = 0

    for floor in range(1, n + 1):
        floor_str = str(floor).zfill(k)
        changes = 0

        for xi, yi in zip(x_str, floor_str):
            changes += count_led_changes(int(xi), int(yi))

        if changes <= p:
            result += 1

    return result - 1  # X층 제외

print(solve(n, k, p, x))