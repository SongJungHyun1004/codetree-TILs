import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
tree = [
    []
    for _ in range(n+1)
]
visited = [False]*(n+1)
for _ in range(n-1):
    s, e, d = map(int, input().split())
    tree[s].append((e, d))
    tree[e].append((s, d))

def dfs(x, dist):
    global mx_node, mx
    if mx < dist:
        mx = dist
        mx_node = x
    visited[x] = True
    for nx, d in tree[x]:
        if not visited[nx]:
            dfs(nx, dist+d)

mx_node, mx = 0, 0
dfs(1, 0)
mx = 0
visited = [False]*(n+1)
dfs(mx_node, 0)
print(mx)