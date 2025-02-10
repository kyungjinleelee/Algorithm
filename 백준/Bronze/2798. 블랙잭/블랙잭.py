from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for combo in combinations(cards, 3):
    total = sum(combo)
    if total <= m:
        max_sum = max(max_sum, total)

print(max_sum)