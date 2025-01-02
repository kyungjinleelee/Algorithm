n, m = map(int, input().split())

# 바구니 리스트 만들기
baskets = []
for index in range(1, n + 1):
    baskets.append(index)

for _ in range(m):
    i, j = map(int, input().split())
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(*baskets)