k = int(input())
inorder = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def make_tree(s, e, depth):
    if s > e:
        return
    mid = (s+e)//2
    tree[depth].append(inorder[mid])
    make_tree(s, mid-1, depth+1)
    make_tree(mid+1, e, depth+1)

n = len(inorder)
make_tree(0, n-1, 0)

for i in tree:
    print(*i)