a, b = map(int, input().split())
c = int(input())

def solution(a, b, c):
    if b + c < 60:
        b = b + c
    elif b + c == 60:
        a += 1
        b = 0
    elif b + c > 60:
        if (b + c) % 60 == 0:
            a += (b + c) // 60
            b = 0
        else:
            a += (b + c) // 60
            b = (b + c) % 60

    if a == 24:
        a = 0
    elif a > 24:
        a -= 24
        
    print(a, b)

solution(a, b, c)