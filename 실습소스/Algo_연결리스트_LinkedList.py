# array와 linked list의 차이
# 어레이: 파이썬의 리스트. 접근 쉬움, 삽입 어려움. (데이터에 접근하는 경우가 빈번하다면 Array를 사용하자)
# 연결 리스트: 직접 구현. 접근 어려움, 삽입 쉬움.  (삽입과 삭제가 빈번하다면 LinkedList를 사용하는 것이 더 좋다)

# 연결 리스트 (구현할 줄 알아야함)
	class ListNode:
		def __init__(self, val, next):	# 네모상자(val)와 화살표(next) 입력받기
			self.val = val		# '나의 val은 입력받은 val이고,
			self.next = next	# 나의 next는 입력받은 next이다' 라고 지정 

	class LinkedList:  	# 삽입, 삭제 기능 기본적으로 있어야함
		# 삽입
		def __init__(self):
			self.head = None		# 아무 자료도 안 들어와있는 것이 디폴트값
		
		def append(self, val):
			if not self.head:			# 만약 self.head가 없다면? (비어있다면)
				self.head = ListNode(val, None) 	# 다음 화살표 요소는 없는 ListNode로 지정을 해줘야함
				return

			# self.head가 있다면 > 쭉쭉 넘어가서 붙여준다.
			node = self.head
			while node.next:		# node의 다음(next, 화살표)이 있는 한
				node = node.next	# 계속 넘어감

			node.next = ListNode(val, None) # 새로 하나 만들어서(ListNode(val, None)) node.next에 붙여준다.는 의미
