n, x = map(int, input().split())
list = list(map(int, input().split()))

answer = []
for li in list:
    if li < x:
        answer.append(li)
print(*answer)