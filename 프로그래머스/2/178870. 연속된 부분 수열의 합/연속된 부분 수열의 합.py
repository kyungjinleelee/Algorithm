def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]  # 초기 부분 수열의 합
    min_length = float('inf')  # 최소 길이를 무한대로 초기화
    answer = []  # 결과를 담을 배열

    while right < len(sequence):
        if current_sum == k:
            # 현재 부분 수열의 길이 계산
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
                answer = [left, right]  # 새로운 최소 길이의 부분 수열 저장
            elif current_length == min_length and (not answer or left < answer[0]):
                answer = [left, right]  # 같은 길이지만 시작 인덱스가 더 작은 경우 갱신

            # 다음 탐색을 위해 부분 수열 축소
            current_sum -= sequence[left]
            left += 1

        elif current_sum < k:
            # 부분 수열의 합이 k보다 작으므로 오른쪽 포인터 확장
            right += 1
            if right < len(sequence):  # 범위 체크
                current_sum += sequence[right]

        else:
            # 부분 수열의 합이 k보다 크므로 왼쪽 포인터 이동
            current_sum -= sequence[left]
            left += 1

    return answer