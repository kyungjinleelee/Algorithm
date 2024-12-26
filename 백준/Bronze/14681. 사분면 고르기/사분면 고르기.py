x = int(input())
y = int(input())

def solution(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 < y:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 > y:
        print(4)

solution(x, y)