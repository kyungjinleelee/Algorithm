list_n = []
for _ in range(10):
    n = int(input())
    list_n.append(n)

division = []
for n in list_n:
    division.append(n % 42)

answer = len(set(division))
print(answer)