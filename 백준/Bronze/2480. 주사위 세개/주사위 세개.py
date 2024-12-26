a, b, c = map(int, input().split())

def calculate_prize(a, b, c):
    prize = 0
    # 모두 같을 경우의 수
    if a == b == c:
        prize = 10000 + a * 1000
    # 두 개만 같을 경우의 수
    elif a == b or b == c or a == c:
        if a == b:
            prize = 1000 + a * 100
        elif b == c:
            prize = 1000 + b * 100
        elif a == c:
            prize = 1000 + c * 100
    # 모두 다를 경우
    else:
        prize = max([a, b, c]) * 100

    print(prize)

calculate_prize(a, b, c)