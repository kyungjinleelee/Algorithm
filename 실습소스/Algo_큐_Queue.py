# 큐 구현
class Node: # 큐의 노드
	def __init__ (self, item, next): # 노드는 두 가지로 구성됨, 내가 갖고있는 값:item, 가르키는 녀석(화살표):next
		self.item = item
		self.next = next

class Queue: # 큐 (먼저 줄 선 사람이 먼저 밥머금)
	def __init__ (self):
		self.front = None  # 제일 앞에 있는 녀석을 지정해주는 것이 제일 중요

	def is_empty(self):		 # 비었는지 안 비었는지 보려면
		return self.front is None  #제일 앞에 있는 녀석이 비었는지 보면 됨 

	def push(self, value):		# 무언가를 넣을 때는
		if not self.front:	# front가 비었다면?
			self.front = Node(value, None) # 새로 만든 노드 넣어주고 종료 
			return

		node = self.front	# front가 안 비었다면?
			while node.next:	# 다음이 존재하는 한 
				node = node.next # 끝까지 가야함 !!

			# 알고리즘이 끝나고 끝까지 도달한 상태
			node.next = Node(value, None)
	
	def pop(self):			# 무언가를 뺄 때
		if not self.front:
			return None	# 비었다면 None을 반환

		node = self.front	# 비지 않았다면 그 값을 반환
		self.front = self.front.next # front를 기존 녀석의 다음 녀석으로 지정
		return node.item
