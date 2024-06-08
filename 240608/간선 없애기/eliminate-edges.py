import sys
import copy
from heapq import heappush, heappop
INF = sys.maxsize
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
edges = []
for _ in range(m):
    s, e, d = map(int, input().split())
    edges.append((s, e, d))
    graph[s].append((e, d))
    graph[e].append((s, d))

def dijkstra(src, dst, tmp):
    dist = [INF]*(n+1)
    dist[src] = 0
    pq = []
    heappush(pq, (0, src))
    while pq:
        now_d, now = heappop(pq)
        if dist[now] < now_d:
            continue
        for nxt, nxt_d in tmp[now]:
            if dist[nxt] > now_d + nxt_d:
                dist[nxt] = now_d + nxt_d
                heappush(pq, (dist[nxt], nxt))
    return dist[dst]
cnt = 0
origin = dijkstra(1, n, graph)
for s, e, d in edges:
    tmp = copy.deepcopy(graph)
    tmp[s].remove((e, d))
    tmp[e].remove((s, d))
    d = dijkstra(1, n, tmp)
    if origin != d:
        cnt += 1
print(cnt)