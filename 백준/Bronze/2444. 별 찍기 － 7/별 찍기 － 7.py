n = int(input())

# 첫 번째 파트
for i in range(1, n + 1):
    space = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(space + stars)

# 두 번째 파트
for i in range(n - 1, 0, -1):
    space = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(space + stars)