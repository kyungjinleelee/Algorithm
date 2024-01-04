	class Node: # 스택의 노드 
		def __init__(self, item, next):	# 노드는 두 가지로 구성됨, 내가 갖고있는 값:item, 가르키는 녀석(화살표):next
			self.item = item
			self.next = next	# 스택의 기본 단위		

	class Stack: # 스택 (한쪽 끝으로만 자료를 넣고 뺄 수 있는 자료 구조)
		def __init__(self):	# 스택의 구성
			self.top = None	# 스택의 제일 위 

		# push, pop, is_empty로 구성
		def is_empty(self):	# 비었는지 안비었는지 보는 방법
			return self.top is None	# top이 비었는지 안 비었는지 보면 됨 

		def push(self, val):		# 밀어넣을 때
			self.top = Node(val, self.top)	# Node를 top으로 지정해주면 됨

		def pop(self):			# 값을 꺼낼 때
			if not self.top:		# top이 비어있다면?
				return None	# None 반환 (아무것도 반환하지 말라는 뜻)

			node = self.top		# 그게 아니라면, top을 꺼내서
			self.top = self.top.next	# 새로운 top을 기존 top의 다음 녀석 (바로 아래에 있는)으로 지정 
			return node.item	# 노드에 값을 반환하셈
