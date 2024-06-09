import sys
from heapq import heappush, heappop

def dijkstra(start, end, avoided_edges):
    dist = [sys.maxsize] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        curr_dist, curr_node = heappop(heap)
        
        if curr_dist > dist[curr_node]:
            continue
        
        for next_node, next_dist in graph[curr_node]:
            if (curr_node, next_node) not in avoided_edges and dist[next_node] > curr_dist + next_dist:
                dist[next_node] = curr_dist + next_dist
                heappush(heap, (dist[next_node], next_node))
    
    return dist[end]

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
avoided_edges = set()

for _ in range(m):
    s, e, d = map(int, sys.stdin.readline().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

dist1 = dijkstra(1, n, avoided_edges)
for u, v in graph[1]:
    avoided_edges.add((1, v))

dist2 = dijkstra(1, n, avoided_edges)
print(-1 if dist2 == sys.maxsize else dist2)