import sys
MAX = sys.maxsize
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)

def dfs(x, dist):
    global mx
    visited[x] = True
    mx = max(mx, dist)
    for nx in tree[x]:
        if not visited[nx]:
            dfs(nx, dist+1)

node = -1
mn_dist = MAX
for i in range(1, n+1):
    visited = [False]*(n+1)
    mx = 0
    dfs(i, 0)
    if mn_dist > mx:
        mn_dist = mx
        node = i
print(mn_dist)