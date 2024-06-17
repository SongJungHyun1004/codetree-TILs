import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
MAX = sys.maxsize
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

def dfs(x, dist):
    global mx, mx_node
    visited[x] = True
    if mx < dist:
        mx = dist
        mx_node = x
    for nx in tree[x]:
        if not visited[nx]:
            dfs(nx, dist+1)

mx_node = -1
visited = [False]*(n+1)
mx = 0
dfs(1, 0)
visited = [False]*(n+1)
mx = 0
dfs(mx_node, 0)
print(mx//2 if mx%2 == 0 else (mx+1)//2)