# 주어진 이진탐색트리(BST)에서 val과 같은 값을 가지는 노드를 반환하는 문제
# 비교적 간단하게 풀었다.

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        # 현재 노드의 값이 찾고자 하는 값과 일치하면 현재 노드를 반환 
        if root.val == val:
            return root

        # 찾고자 하는 값이 현재 노드의 값보다 작으면 왼쪽 서브트리에서 탐색
        if val < root.val:
            return self.searchBST(root.left, val)

        # 찾고자 하는 값이 현재 노드의 값보다 크면 오른쪽 서브트리에서 탐색
        if val > root.val:
            return self.searchBST(root.right, val)
