n = int(input()) # 노드의 갯수
tree = {} # 트리를 저장할 딕셔너리

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(node):
    if node == '.':
        return ''
    return node + preorder(tree[node][0]) + preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return ''
    return inorder(tree[node][0]) + node + inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return ''
    return postorder(tree[node][0]) + postorder(tree[node][1]) + node

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))