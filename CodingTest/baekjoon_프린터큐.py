t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # 케이스 문서의 수 n, 출력 순서를 모르는 문서의 현재 위치 m 입력받기
    data = list(map(int, input().split()))	# 문서의 우선순위가 저장된 리스트 data를 입력받음
    
    count = 1					# 초기화
    while data:
        if data[0] < max(data):		# 현재 문서의 우선순위가 가장 높은지 확인
            data.append(data.pop(0))
        else: 
            if m == 0: break
                
            data.pop(0)			# 출력이 이루어지면 해당 문서를 제거한 후
            count += 1			# count 증가시킴
            
        m = m -1 if m > 0 else len(data) - 1   # 우선순위가 가장 높지 않은 경우, 문서를 맨 뒤로 이동시키고 m값 조정
 print(count)				# 반복문 종료 시 테스트 결과인 count 출력
