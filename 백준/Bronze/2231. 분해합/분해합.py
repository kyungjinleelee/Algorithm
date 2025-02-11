def find_constructor(N):
    # 가능한 최소 생성자부터 탐색 (N - 9 * 자리수 개수)
    start = max(1, N - (9 * len(str(N))))

    for M in range(start, N):
        # 분해합 계산
        total = M + sum(map(int, str(M)))
        if total == N:
            return M  # 가장 작은 생성자 찾으면 반환

    return 0  # 생성자가 없으면 0 반환

N = int(input())
print(find_constructor(N))