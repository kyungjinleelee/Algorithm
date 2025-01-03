S = str(input())

list_s = []
for s in S:
    list_s.append(s)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = []
for a in alphabet:
    if a in list_s:
        result.append(list_s.index(a))
    else:
        result.append(-1)

print(*result)