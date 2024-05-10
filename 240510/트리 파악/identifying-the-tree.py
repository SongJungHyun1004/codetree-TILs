import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)

def dfs(x):
    global dist
    visited[x] = True
    for nx in tree[x]:
        if not visited[nx]:
            dist += 1
            dfs(nx)

visited = [False]*(n+1)
dist = 0
dfs(1)
print(1 if dist%2 else 0)