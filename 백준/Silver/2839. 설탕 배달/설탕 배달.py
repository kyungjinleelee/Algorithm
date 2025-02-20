n = int(input())

def min_sugar(n):
    # 5kg 봉지를 최대한 많이 사용하는 방향으로 탐색
    for x in range(n // 5, -1, -1):
        # 5kg 봉지를 x개 사용하고 남은 무게
        remain = n - (x * 5)
        if remain % 3 == 0:
            y = remain // 3
            return x + y # 총 봉지 갯수

    return -1

print(min_sugar(n))