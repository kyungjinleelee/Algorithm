n = int(input())
sequence = list(map(int, input().split()))

def count_unique_sequences(n, sequence):
    # 중복 확인을 위한 집합
    seen = set()
    start = 0
    cnt = 0

    # 투포인터로 연속 부분 수열 탐색
    for end in range(n):
        # 중복 제거를 위해 start를 이동
        while sequence[end] in seen:
            seen.remove(sequence[start])
            start += 1

        # 현재 숫자를 집합에 추가
        seen.add(sequence[end])

        # 경우의 수 계산
        cnt += (end - start + 1)

    return cnt

print(count_unique_sequences(n, sequence))