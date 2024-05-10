import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
tree = [[] for _ in range(n+1)]
dist = [0]*(n+1)
visited = [False] * (n+1)
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(x):
    global result
    if len(tree[x]) == 1:
        result += dist[x]
    visited[x] = True
    for nx in tree[x]:
        if not visited[nx]:
            dist[nx] = dist[x]+1
            dfs(nx)
result = 0
dfs(1)
print(1 if result % 2 else 0)