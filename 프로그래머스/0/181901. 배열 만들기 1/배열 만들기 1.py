def solution(n, k):
    answer = []
    # <1부터 n까지 수 중에서 k의 배수를 찾아서 배열에 저장하기>
    # 1부터 n까지 반복 
    for i in range(1, n + 1):
        # 현재 숫자가 k의 배수이면 리스트에 추가
        if i % k == 0:
            answer.append(i)
    return answer