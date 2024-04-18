import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

a, b = map(int, input().split())

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

print(dijkstra(a, b))