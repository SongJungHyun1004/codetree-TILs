n = int(input())

tree = {}
for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)

def visit(node):
    print(node, end='')

def preorder(node):
    (left, right) = tree[node]
    visit(node)
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

def inorder(node):
    left, right = tree[node]
    if left != '.':
        inorder(left)
    visit(node)
    if right != '.':
        inorder(right)

def postorder(node):
    left, right = tree[node]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    visit(node)

root = 'A'
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()