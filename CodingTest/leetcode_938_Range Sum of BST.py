# 주어진 범위 내에 있는 모든 노드의 값을 합산하는 문제

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):      # node: 현재 노드
            if not node:    # node가 None이면 0 반환
                return 0

            if node.val < low: # 현재 노드의 값이 최소값보다 작으면 
                return dfs(node.right)  # 오른쪽 서브트리 탐색

            if node.val > high: # 현재 노드의 값이 최대값보다 크면
                return dfs(node.left)   # 왼쪽 서브트리 탐색

            # 현재 노드의 값이 최소값과 최대값 범위 사이에 있으면
            # 현재 노드 값 + dfs(왼쪽 서브트리) + dfs(오른쪽 서브트리)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
        # root: BST의 루트 노드
        # low: 최소값 범위, high: 최대값 범위

"""
로직을 생각해보자
주어진 트리: [10, 5, 15, 3, 7, null, 18]

1. rangeSumBST 메소드가 호출되면, dfs(root)가 실행됨.
2. dfs 함수가 루트 노드 10에서 시작
3. 10은 low와 high의 범위 [7, 15]에 속하므로, 10의 값을 합산
4. 이어서 왼쪽 서브트리에 대해 dfs(node.left)가 호출 > 왼쪽 자식인 5로 이동
5. 5도 [7, 15] 범위에 속하므로, 5의 값을 합산
6. dfs(node.left) 호출시 왼쪽 자식인 3으로 이동
7. 3도 [7, 15] 범위에 속하므로, 3의 값을 합산
8. dfs(node.left) 호출시 더 이상 왼쪽 자식이 없으므로 0을 반환하게됨
9. 이어서 오른쪽 서브트리에 대해 dfs(node.right)가 호출 > 오른쪽 자식인 7로 이동
10. 7도 [7, 15] 범위에 속하므로, 7의 값을 합산
11. dfs(node.right) 호출시 왼쪽 자식인 null로 이동 > 이때 null은 0을 반환
12. 다시 루트 노드인 10으로 돌아와서 오른쪽 서브트리에 대해 dfs(node.right)를 호출 > 오른쪽 자식인 15로 이동
13. 15도 [7, 15] 범위에 속하므로, 15의 값을 합산
14. dfs(node.right) 호출시 왼쪽 자식인 18로 이동. 18은 [7, 15] 범위를 벗어나므로 dfs(node.left)가 호출되어 0을 반환
15. 모든 서브트리를 순회한 후 최종적으로 32가 반환. (10 + 5 + 7 + 15)
따라서 이 트리에서 [7, 15] 범위에 속하는 노드들의 값을 합산하면 32가 됨!
"""
