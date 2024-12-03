n = int(input())
numbers = list(map(int, input().split()))
operator_count = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

def dfs(idx, current_result, plus, minus, multiply, divide):
    global max_result, min_result
    if idx == n:  # 모든 숫자를 다 사용했으면 결과 갱신
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return

    # 각 연산자를 사용해 다음 재귀 호출
    if plus > 0:
        dfs(idx + 1, current_result + numbers[idx], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(idx + 1, current_result - numbers[idx], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(idx + 1, current_result * numbers[idx], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(idx + 1, int(current_result / numbers[idx]), plus, minus, multiply, divide - 1)

# DFS 시작
dfs(1, numbers[0], operator_count[0], operator_count[1], operator_count[2], operator_count[3])

print(max_result)
print(min_result)