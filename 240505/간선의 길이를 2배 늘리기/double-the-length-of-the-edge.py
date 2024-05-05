from heapq import heappush, heappop
import sys
import copy
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
m_lst = []
for _ in range(m):
    s, e, d = map(int, input().split())
    m_lst.append((s, e, d))
    graph[s].append((e, d))
    graph[e].append((s, d))

def dijkstra(src, dst, graph):
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

origin = dijkstra(1, n, graph)
mx = 0
for s, e, d in m_lst:
    graph[s][graph[s].index((e, d))] = (e, 2*d)
    graph[e][graph[e].index((s, d))] = (s, 2*d)
    val = dijkstra(1, n, graph)
    mx = max(mx, val)
    graph[s][graph[s].index((e, 2*d))] = (e, d)
    graph[e][graph[e].index((s, 2*d))] = (s, d)
print(mx-origin)