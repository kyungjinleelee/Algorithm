h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
# 첫 번째 칸과 마지막 칸은 물이 고일 수 없음
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        ans += compare - world[i]

print(ans)