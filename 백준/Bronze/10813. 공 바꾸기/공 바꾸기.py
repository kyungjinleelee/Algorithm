n, m = map(int, input().split())

buckets = []
for i in range(1, n + 1):
    buckets.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    buckets[i - 1], buckets[j - 1] = buckets[j - 1], buckets[i - 1]

print(*buckets)