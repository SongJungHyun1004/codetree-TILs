n = int(input())
parent = list(map(int, input().split()))
remove = int(input())

for i in range(n):
    if parent[i] == remove:
        parent[i] = -1
parent[remove] = -1

tree = [
    []
    for _ in range(n)
]
for i in range(n):
    if parent[i] != -1:
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
dfs(0)
print(cnt)