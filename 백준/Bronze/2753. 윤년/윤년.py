year = int(input())

def solution():
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(1)
    else:
        print(0)

solution()