# 첫 번째 입력: 정수의 개수 N
N = int(input())

# 두 번째 입력: N개의 정수를 리스트로 저장
numbers = list(map(int, input().split()))

# 세 번째 입력: 찾으려는 정수 v
v = int(input())

# numbers 리스트에서 v의 등장 횟수 출력
print(numbers.count(v))