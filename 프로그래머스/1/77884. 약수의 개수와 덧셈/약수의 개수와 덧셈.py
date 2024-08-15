def solution(left, right):
    total = 0
    for num in range(left, right + 1):
        if int(num ** 0.5) ** 2 == num:
            total -= num
        else:
            total += num
    return total