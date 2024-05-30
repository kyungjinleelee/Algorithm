def solution(n):
    cnt = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1         # (i, n // i) 한 쌍
            if i != n // i:
                cnt += 1     # (n // i, i) 한 쌍
    return cnt