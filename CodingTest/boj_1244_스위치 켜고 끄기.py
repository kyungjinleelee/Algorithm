# 일정 규칙에 따라 학생들이 스위치를 조작하고 난 후의 스위치 상태를 구하는 문제
"""
1. 공통적으로 스위치가 꺼져있으면 키고, 켜져있으면 끄는 행동을 수행하므로 (청개구린가) 스위치 상태 바꾸는 함수를 만들어주자.
2. 남자, 여자의 경우를 따로 생각하자.
2-1. 남자의 경우 
받은 스위치 번호의 배수 번호의 스위치를 바꾼다. range의 간격을 이용해서 배수를 찾도록 했다.
2-2. 여자의 경우
여자의 경우, 양쪽을 탐색해서 좌우대칭을 찾아줘야 하므로 /2 대신, 정수부분만을 취하는 //2 로 전체 길이를 탐색하도록 해줬다.
3. 주의: 문제 출력 조건 주의
"""

from sys import stdin
input = stdin.readline

def change(num):			# 스위치 상태 바꾸는 함수
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

n = int(input())	        # 스위치 갯수
switch = [0] + list(map(int, input().split()))		# 스위치의 초기 상태 (인덱스 1부터 시작하게 하기 위해 + [0])
students = int(input())		# 학생 수
for _ in range(students):
    sex, num = map(int, input().split())	# sex: 학생들의 성별, num: 스위치 번호 입력받기
    # 남자
    if sex == 1:		      # 만약에 남자면
        for i in range(num, n+1, num):		# 번호의 배수에 해당하는 스위치를 조작함
            change(i)				# change함수 호출
    # 여자
    else:					# 여자면! 
        change(num)			# change함수 호출
        for k in range(n // 2):		# 좌우 대칭인 범위 확인
            if num + k > n or num - k < 1: # 범위 벗어나면 break
               break
            if switch[num + k] == switch[num - k]:	# (좌우대칭인 범위 내에서) 스위치 상태가 동일하면, 스위치 상태 변경
                change(num + k)			# 좌우대칭인 스위치 중 우측의 스위치 상태 변경
                change(num - k)			# 좌측의 상태도 변경 
            else:									  # (좌우대칭인 범위 내에서) 스위치 상태 다르면 break
                break
                
for i in range(1, n+1):			    	# 1부터 n까지
    print(switch[i], end = " ")		# 출력 값 사이에 공백 넣어서 출력 (end = " ")
    if i % 20 == 0 :				      # 20개씩 스위치 출력 후,
        print()						        # 새로운 행으로 넘어가셈
