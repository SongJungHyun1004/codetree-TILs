from heapq import heappush, heappop
n = int(input())
pq = []
for _ in range(n):
    x = int(input())
    if x:
        heappush(pq, -x)
    else:
        if pq:
            print(-heappop(pq))
        else:
            print(0)