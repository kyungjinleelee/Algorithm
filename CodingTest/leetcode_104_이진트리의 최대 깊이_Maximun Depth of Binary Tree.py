"""
트리에서 깊이(Depth)는 루트에서부터 현재 노드까지의 거리이다.
최대 깊이는 리프 노드까지 거리 중 가장 긴 거리를 구하면 된다.
"""
# 반복 구조 Deque
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:               # root가 None인 경우, 빈 큐로 시작하도록 함
            return 0               # 이 코드 없으면 while문 무한루프 빠진다 .. 

        q = deque([root])          # root 넣어줌
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):    # root 꺼냄
                cur = q.popleft()
                if cur.left:           # current에서 왼쪽, 오른쪽 노드가 있다면, (없다면 넘어가)
                    q.append(cur.left)  # q에 집어넣으셈
                if cur.right:
                    q.append(cur.right)

        return depth
