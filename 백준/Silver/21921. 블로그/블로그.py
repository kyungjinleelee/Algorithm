N, X = map(int, input().split())
visitors = list(map(int, input().split()))

def blog(N, X, visitors):
    # 초기값 설정
    current_sum = sum(visitors[:X])  # 첫 번째 X일 합
    max_sum = current_sum  # 최대 방문자 수
    count = 1  # 최대 방문자 수를 기록한 기간의 개수

    # 슬라이딩 윈도우
    for i in range(X, N):
        current_sum += visitors[i] - visitors[i - X]
        if current_sum > max_sum:
            max_sum = current_sum
            count = 1  # 새로운 최대값이 나오면 카운트 초기화
        elif current_sum == max_sum:
            count += 1  # 최대값과 동일한 경우 카운트 증가

    # 결과 출력
    if max_sum == 0:
        print("SAD")
    else:
        print(max_sum)
        print(count)

blog(N, X, visitors)