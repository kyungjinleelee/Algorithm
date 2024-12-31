n, m = map(int, input().split())

buckets= [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i - 1, j):
        buckets[index] = k # k번 공 넣기

print(*buckets)