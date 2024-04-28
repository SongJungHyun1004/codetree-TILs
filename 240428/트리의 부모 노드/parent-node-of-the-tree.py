import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
tree = [
    []
    for _ in range(n+1)
]
parent = [0]*(n+1)
visited = [False]*(n+1)
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(x):
    visited[x] = True
    for nx in tree[x]:
        if not visited[nx]:
            parent[nx] = x
            dfs(nx)

dfs(1)
for i in range(2, n+1):
    print(parent[i])