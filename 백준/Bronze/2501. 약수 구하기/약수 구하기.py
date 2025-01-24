n, k = map(int, input().split())

# 약수 리스트 구하기
divisor = []
for i in range(1, n + 1):
    if n % i == 0:
        divisor.append(i)

# n의 약수 중 k번째로 작은 수 출력하기
if len(divisor) >= k:
    answer = divisor[k - 1]
    print(answer)
else:
    print(0)