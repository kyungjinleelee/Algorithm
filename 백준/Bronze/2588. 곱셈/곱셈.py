num1 = int(input())
num2 = int(input())

list_b = list(str(num2))
def solution():
    first = num1 * int(list_b[2])
    second = num1 * int(list_b[1])
    third = num1 * int(list_b[0])
    print(first)
    print(second)
    print(third)
    print(first + second * 10 + third * 100)

solution()
