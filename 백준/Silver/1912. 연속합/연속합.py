n = int(input())
arr = list(map(int, input().split())) # [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

current_max = arr[0]
global_max = arr[0]

for i in range(1, n):
    current_max = max(current_max + arr[i], arr[i])
    global_max = max(global_max, current_max)

print(global_max)