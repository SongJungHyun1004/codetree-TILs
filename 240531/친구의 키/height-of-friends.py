import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
order = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(x):
    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)
    order.append(x)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

print(*order[::-1])