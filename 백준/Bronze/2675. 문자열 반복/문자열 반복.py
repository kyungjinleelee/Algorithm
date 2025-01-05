t = int(input())
list = [list(map(str, input().split())) for _ in range(t)]

p = ''
for i in range(len(list)):
    for j in range(len(list[i][-1])):
        p += list[i][-1][j] * int(list[i][0])
    p += '\n'
print(p)