from heapq import heappop, heappush
import sys
INF = sys.maxsize
input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())
graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))
    graph[e].append((s, v))

def dijkstra(src):
    dist = [INF]*(n+1)
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        now_d, now = heappop(pq)
        if dist[now] < now_d:
            continue
        for nxt, nxt_d in graph[now]:
            if dist[nxt] > now_d+nxt_d:
                dist[nxt] = now_d+nxt_d
                heappush(pq, (dist[nxt], nxt))
    return dist

dist = dijkstra(k)
for i in range(1, n+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])