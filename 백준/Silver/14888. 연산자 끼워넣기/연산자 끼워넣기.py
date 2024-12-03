from itertools import permutations

# 입력 받기
n = int(input())
numbers = list(map(int, input().split())) # 숫자 리스트
operator_count = list(map(int, input().split())) # 연산자 갯수: [+, -, *, /]

# 연산자 리스트 생성
operators = []
for i, op in enumerate(["+", "-", "*", "/"]):
    operators.extend([op] * operator_count[i])

# 모든 연산자 순열 생성
operator_permutations = set(permutations(operators, n - 1))

# 계산 함수
def calculate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "-":
            result -= numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
        elif operators[i] == "/":
            # 나눗셈은 정수 몫만 취함
            if result < 0:
                result = -(-result // numbers[i + 1])
            else:
                result //= numbers[i + 1]
    return result

# 최댓값과 최솟값 계산
max_result = -float('inf')
min_result = float('inf')

for ops in operator_permutations:
    result = calculate(numbers, ops)
    max_result = max(max_result, result)
    min_result = min(min_result, result)

# 결과 출력
print(max_result)
print(min_result)