import sys
input = sys.stdin.readline
from heapq import heappush, heappop
INF = sys.maxsize
n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, d = map(int, input().split())
    tree[s].append((e, d))
    tree[e].append((s, d))

def dijkstra(src, dst):
    dist = [INF]*(n+1)
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        now_d, now = heappop(pq)
        if dist[now] < now_d:
            continue
        for nxt, nxt_d in tree[now]:
            if dist[nxt] > now_d + nxt_d:
                dist[nxt] = now_d + nxt_d
                heappush(pq, (dist[nxt], nxt))
    return dist[dst]

for _ in range(m):
    a, b = map(int, input().split())
    print(dijkstra(a, b))