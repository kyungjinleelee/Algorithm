h, m = map(int, input().split())

def solution(h, m):
    if m >= 45:
        m -= 45
    elif m - 45 < 0:
        m = (60 + m) - 45
        if h == 0:
            h = 23
        else:
            h -= 1
    print(h, m)

solution(h, m)