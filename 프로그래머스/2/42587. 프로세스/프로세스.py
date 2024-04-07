"""
queue 구현의 경우 deque의 pop()이 list의 pop(0)보다 빠름
"""
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    
    while queue:
        # 큐 안의 가장 높은 우선순위 구하기
        m = max(queue)
        # 큐에서 가장 앞에 위치하는 프로세스 구하기 
        l = queue.popleft()
        location -= 1
        # 가장 앞 프로세스가 max priority가 아니라면 다시 큐에 넣기 
        if l != m:
            queue.append(l)
            # 프로세스의 위치가 0보다 작다면 (이미 빠져나갔다면)
            if location < 0:
                # 큐의 길이에서 1 뺀 값 위치로 설정
                location = len(queue) - 1
        # 가장 앞 프로세스가 max priority일 경우 
        else:
            answer += 1
            if location < 0:
                break
    
    return answer