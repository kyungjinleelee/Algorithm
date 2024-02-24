def solution(n, k, cmd):
    global stack, deleteNum, cur, record
    cur = k
    record = []
    stack = []
    deleteNum = [1] * n
    
    #record 배열 선언
    for i in range(n):
        record.append([i-1, i+1])
        
    # 0번째 요소의 prev와  n번째 요소의 next를 -1로 선언 
    record[0][0] = -1
    record[n-1][1] = -1
    
    for command in cmd:
        if (len(command) == 1):
            if command == "C":
                delete()
            else:
                resotre()
        else:
            c, num = command.split()
            move(c, int(num))
                   
        answer = ''
    for i in deleteNum:
        if i == 1:
            answer += 'O'
        else:
            answer += 'X'
    
    return answer
    
# 현재 위치 이동 함수
def move(command, num):
    global cur, record
    cnt = 0
    
    if command == 'U':
    	# num 만큼 반복 
        for _ in range(num):
        	# 0번째 인덱스가 prev를 의미하므로 prev를 현재 위치로 변경
            cur = record[cur][0]
    
    if command == 'D':
        for _ in range(num):
        	# 0번째 인덱스가 next를 의미하므로 next를 현재 위치로 변경
            cur = record[cur][1]
            
# 복구 함수
def resotre():
    global deleteNum, cur, stack, record
    
    # 복구할 요소 반환
    restore = stack.pop()
    prev, next = record[restore]
    
    deleteNum[restore] = 1
    
   	# prev가 -1인 경우 첫 번째 요소였기 때문에 next 요소만 변경
    if prev == -1:
        record[next][0] = restore
	# next가 -1인 경우 마지막 요소였기 때문에 prev 요소만 변경
    elif next == -1:
        record[prev][1] = restore

    else:
        record[next][0] = restore
        record[prev][1] = restore
        
# 삭제 함수
def delete():
    global deleteNum, cur, stack, record
    
    # 삭제 표시 및 복구를 위한 스택 배열에 요소 추가
    deleteNum[cur] = 0
    stack.append(cur)
    
    prev, next = record[cur]
        
    # 삭제할 요소의 next가 -1인 경우 마지막 요소이기 때문에 현재 위치를 prev로 설정
    if next == -1:
        cur = record[cur][0]
    
    else:
        cur = record[cur][1]
    
    # prev가 -1인 경우 삭제할 요소가 첫 번째 요소이기 때문에 next 요소가 첫 번째 요소가 된다.
    if prev == -1:
        record[next][0] = -1
    
    # next가 -1인 경우 삭제할 요소가 마지막 요소이기 때문에 prev요소가 마지막 요소가 된다.
    elif next == -1:
        record[prev][1] = -1
        
    else:
        record[prev][1] = next
        record[next][0] = prev
