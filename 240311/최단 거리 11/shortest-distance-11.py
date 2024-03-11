from heapq import heappush, heappop
import sys
INF = sys.maxsize
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [
    []
    for _ in range(n+1)
]
for _ in range(m):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))
for i in range(1, n+1):
    graph[i] = sorted(graph[i], reverse=True)
a, b = map(int, input().split())

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

dist = dijkstra(a)
print(dist[b])
x = b
lst = [x]
while x != a:
    for i, d in graph[x]:
        if dist[i] + d == dist[x]:
            x = i
            lst.append(x)
            break
    
print(*lst[::-1])