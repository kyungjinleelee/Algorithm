# 그리디 알고리즘
# 사람 수와 각 사람마다 돈을 인출하는 데 걸리는 시간을 입력받고, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하는 문제

n = int(input())    # 사람의 수 
p = list(map(int, input().split()))    # 각 사람이 돈을 인출하는 데 걸리는 시간을 저장한 리스트

p.sort()    # 오름차순 정렬
result = 0

for i in range(1, n + 1):
    result += sum(p[0:i])    # p[0:i]는 리스트 p의 0번째 인덱스부터 i-1번째 인덱스까지의 부분 리스트를 의미
    
print(result)
