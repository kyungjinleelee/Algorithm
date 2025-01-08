s = input()

def longest_kkrukk(s):
    # 왼쪽과 오른쪽 K의 누적 개수를 저장할 리스트
    left_k, right_k = [], []

    # 문자열에서 왼쪽 기준 K 개수 누적
    cnt = 0
    for c in s:
        if c == 'K':
            cnt += 1
        else:
            left_k.append(cnt)

    # 문자열에서 오른쪽 기준 K 개수 누적
    cnt = 0
    for c in s[::-1]:
        if c == 'K':
            cnt += 1
        else:
            right_k.append(cnt)

    # 오른쪽 리스트 뒤집기
    right_k.reverse()

    # 투 포인터 초기화
    l, r = 0, len(left_k) - 1
    ans = 0

    # 투 포인터를 활용해 최대 길이 계산
    while l <= r:
        # 현재 부분 수열의 길이 계산
        ans = max(ans, (r - l + 1) + 2 * min(left_k[l], right_k[r]))

        # 왼쪽과 오른쪽 K 개수 비교 후 포인터 이동
        if left_k[l] < right_k[r]:
            l += 1
        else:
            r -= 1
    return ans


print(longest_kkrukk(s))