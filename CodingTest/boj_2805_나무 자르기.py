# N: 나무의 수, M: 상근이가 집에 가져가려고 하는 나무의 길이
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력하는 문제

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)    # 이진 탐색을 위해 시작 위치와 끝 위치 지정
    
result = 0 # 최종 절단기 높이
while(start <= end):        # 시작 위치가 끝 위치를 넘지 않을 때까지 반복
    mid = (start + end) // 2
    total = 0                # 자른 나무의 길이를 합산할 변수
    for h in trees:
        if h > mid:    # 현재 위치(mid)보다 높이가 커야지만 자를 수 있음
            total += h - mid    # 자른 나무의 길이를 합산
        # 이진 탐색    
    if total < m: # 합산된 자른 나무의 길이가 m(가져가려는 길이)보다 작으면
        end = mid - 1    # mid 기준 왼쪽 부분 탐색
    else:    # m보다 크거나 같으면
        result = mid      # 최종 절단기 높이를 mid로 설정
        start = mid + 1   # mid 기준 오른쪽 부분 탐색
print(result)
