from heapq import heapify, heappush, heappop

a = [5, 3, 4, 1, 2]
heapify(a)	# a를 자료구조로 만들어 줘! 라는 의미 -> a: [1, 2, 4, 3, 5]  
# a 자체는 리스트 자료구조로 저장되었지만 heapify를 통해 heap 자료구조와 비슷하게 인덱스 배열이 바뀐 형태
# 우리가 볼 때는 리스트지만 heap구조로 되어있다는 말 
# 0번 인덱스 값은 heap의 최솟값임
# 하지만 0 이외의 인덱스는 큰 의미가 없으므로 주의
print(a[0])		# 1
print(heappop(a))	# 1 (heappop: heap에서 제일 작은 원소를 뽑아내라) -> a: [2, 3, 4, 5]
print(a[0])		# 2

heappush(a, 7)		# 원소 7을 집어넣겠다는 말 -> a: [2, 3, 4, 5, 7]
print(a[0])		# 2

heappush(a, 0)		# 원소 0을 집어넣겠다는 말 -> a: [0, 3, 2, 5, 7, 4] (임의로 리스트의 순서를 바꿔줌)
print(a[0])		# 0
