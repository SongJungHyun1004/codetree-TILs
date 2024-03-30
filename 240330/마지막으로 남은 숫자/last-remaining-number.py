from heapq import heapify, heappush, heappop
n = int(input())
MIN = 1
arr = list(map(int, input().split()))
pq = [-i for i in arr]
heapify(pq)
while len(pq) > MIN:
    first = -heappop(pq)
    second = -heappop(pq)
    gap = first - second
    if gap:
        heappush(pq, -gap)

if pq:
    print(-pq[0])
else:
    print(-1)