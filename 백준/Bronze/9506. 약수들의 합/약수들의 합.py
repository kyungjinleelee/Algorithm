def solution(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    # 약수들의 합 계산
    divisor_sum = sum(divisors)

    # 완전수 판별
    if divisor_sum == n:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")


while True:
    n = int(input())
    if n == -1:
        break
    solution(n)