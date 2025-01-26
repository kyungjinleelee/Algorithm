n = int(input())
numbers = list(map(int, input().split()))

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
for num in numbers:
    if is_prime(num):
        count += 1

print(count)