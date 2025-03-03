# 응시자 수와 상을 받는 사람의 수 입력 받기
N, K = map(int, input().split())
x = list(map(int, input().split()))

# 점수를 정렬한 후 커트라인을 찾고 출력
sorted_x = sorted(x)
cutline = sorted_x[-K]
print(cutline)