# 터널에들어갔다가 나오는 차량 중 추월한 차량의 개수를 찾는 문제 

N = int(input())    # 터널에 들어가는 차량 입력받기
entry = {input().rstrip() : i for i in range(N)} # 자동차의 입구 순서를 입력받아 딕셔너리 entry에 저장
exit = list(int(entry[input().rstrip()]) for _ in range(N)) # 자동차의 출구 순서를 입력받아 해당 자동차의 인덱스를 리스트 exit에 저장

cnt = 0    # 결과값 변수 초기화
for i in range(N):    # 모든 자동차에 대해 반복
    for j in range(i, N):    # i 이후의 자동차에 대해 반복
        if exit[i] > exit[j]:   # 만약 i번째 자동차가 j번째 자동차보다 먼저 나가면
            cnt += 1            # 1 증가
            break
print(cnt)
