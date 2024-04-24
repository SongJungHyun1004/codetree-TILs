from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
a, b, c  = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

def dijkstra(src, dst):
    dist = [INF]*(n+1)
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        now_d, now = heappop(pq)
        if dist[now] < now_d:
            continue
        for nxt, nxt_d in graph[now]:
            if dist[nxt] > now_d + nxt_d:
                dist[nxt] = now_d + nxt_d
                heappush(pq, (dist[nxt], nxt))
    return dist[dst]

mx = 0
for i in range(1, n+1):
    mn_dist = min(dijkstra(a, i), dijkstra(b, i), dijkstra(c, i))
    mx = max(mx, mn_dist)
print(mx)