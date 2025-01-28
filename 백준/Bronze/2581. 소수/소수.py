m = int(input())
n = int(input())

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

answer = []
for num in range(m, n + 1):
    if is_prime(num):
        answer.append(num)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))