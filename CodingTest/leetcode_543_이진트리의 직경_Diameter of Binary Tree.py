"""
이진 트리의 지름(Diameter)을 계산하는 문제.
트리의 지름은 트리 상의 두 노드 간의 가장 긴 경로의 길이를 나타냄.
트리의 지름을 구하기 위해서는 각 노드에서의 높이를 계산하고, 각 노드를 루트로 하는 서브트리에서의 최대 지름을 구해야 함.
"""
"""
nonlocal: 중첩된 함수에서 외부 함수의 변수를 사용할 때 nonlocal 키워드 사용함
이를 통해 height_and_diameter 함수에서 계산된 최대 지름을 외부 함수인 diameterOfBinaryTree의 max_diameter에 반영할 수 있음
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height_and_diameter(node): # 노드의 높이와 최대 지름을 계산하는 함수
            nonlocal max_diameter
            if not node:    # 노드가 None이면 높이는 0 반환
                return 0

            # 왼쪽, 오른쪽 각 리프 노드까지 탐색(재귀적)
            left_height = height_and_diameter(node.left)
            right_height = height_and_diameter(node.right)

            # 현재까지 계산된 트리의 최대 지름을 기존값과 비교해서 갱신
            max_diameter = max(max_diameter, left_height + right_height)

            # 현재 노드의 높이 반환
            # 1을 더해줌으로써 현재 노드의 깊이 포함시킴
            return 1 + max(left_height, right_height)

        if not root:    # 트리가 비었을 경우 지름도 0임
            return 0

        max_diameter = 0
        height_and_diameter(root)  # 주어진 트리의 루트에서부터 함수 호출, 높이와 지름 계산

        return max_diameter
"""
현재 노드를 포함한 서브트리의 지름 = 해당 노드의 왼쪽 서브트리의 높이 + 오른쪽 서브트리의 높이 
따라서 이 값을 기존 max_diameter와 비교하여 더 큰 값으로 갱신
"""
