def prime_factorization(n):
    # 2부터 시작하여 소인수를 찾음
    factor = 2
    while n > 1:
        while n % factor == 0:
            print(factor)
            n //= factor
        factor += 1 # 다음 숫자로 이동

n = int(input())

# N이 1이면 아무것도 출력하지 않음
if n > 1:
    prime_factorization(n)