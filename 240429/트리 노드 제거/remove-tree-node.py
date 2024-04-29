n = int(input())
parent = list(map(int, input().split()))
remove = int(input())
root = 0
for i in range(n):
    if parent[i] == -1:
        root = i
    if parent[i] == remove:
        parent[i] = -2
parent[remove] = -2

tree = [
    []
    for _ in range(n)
]
for i in range(n):
    if parent[i] > 0:
        tree[i].append(parent[i])
        tree[parent[i]].append(i)

def dfs(x):
    global cnt
    visited[x] = True
    isLeaf = True
    for nx in tree[x]:
        if not visited[nx]:
            isLeaf = False
            dfs(nx)
    if isLeaf:
        cnt += 1

visited = [False]*n
cnt = 0
if tree[root]:
    dfs(root)
print(cnt)