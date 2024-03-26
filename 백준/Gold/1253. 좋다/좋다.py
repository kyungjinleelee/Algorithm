import sys
input = sys.stdin.readline

n = int(input())
number_list = list(map(int, input().split()))
answer = 0
number_list.sort()

for i in range(n):
    find = number_list[i]
    start = 0
    end = n - 1
    while start < end:
        good = number_list[start] + number_list[end]
        if good == find:
            if start != i and end != i:
                answer += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif good < find:
            start += 1
        else:
            end -= 1
        
print(answer)