def min_operations(A, B):
    # B -> A 역으로 접근
    operations = 0
    while B != A:
        if B < A:
            return -1
        if B % 10 == 1:
            B //= 10
        elif B % 2 == 0:
            B //= 2
        else:
            return -1
        operations += 1
    return operations + 1

# 입력
A, B = map(int, input().strip().split())

# 결과 출력
print(min_operations(A, B))