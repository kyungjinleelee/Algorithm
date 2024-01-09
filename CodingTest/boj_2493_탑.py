"""
문제링크:https://www.acmicpc.net/problem/2493
"""
import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))
answer = [0] * n
stack = []

for i in range(len(tops)):
    while stack:		# 스택이 비어있지 않은 동안에 반복
        if tops[stack[-1][0]] < tops[i]:    # 현재 탑보다 높이가 낮다면
            stack.pop()                    # 신호 수신 불가 > 스택에서 pop
        else:	 # 현재 탑보다 크거나 같은 탑
            answer[i] = stack[-1][0] + 1  # 수신받는 탑의 인덱스+1을 정답에 저장
            break
    stack.append((i, tops[i]))
print(*answer)        # iterable 요소 쉽게 풀어서 출력


# 다른 풀이 

n = int(input())                         # 탑의 개수 n
tower = list(map(int, input().split()))  # 탑의 높이를 나타내는 리스트 tower
answer = [0] * n

# 타워의 최대 높이 : 10 ** 8 (10의 8승)
# stack의 값들은 (탑의 높이, 탑의 위치)로 해주자
stack = [(10 ** 8 + 1, 0)]

for i in range(n):
  h = tower[i]   # 탐색하는 위치의 탑 높이를 h로 받아줌
  # 현재 위치(h)보다 왼쪽에 있는 탑 중, 더 낮은 탑은 확인할 필요 x
  while stack[-1][0] < h:
    stack.pop()
  # while문 탐색이 끝났다 = stack 마지막 값이 우리가 찾는 탑의 (높이, 위치)
  # stack이 비어 있지 않은 이유 : 초기값 설정 (즉, 초기값이 항상 탑중에 제일 클거라서 다른 조건문 없이 진행할 수 있음)
  answer[i] = stack[-1][1]
  stack.append((h, i + 1))    # 탑의 높이(h), 위치(i+1)를 append
  
print(*answer)
