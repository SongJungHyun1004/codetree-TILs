from heapq import heappush, heappop

n = int(input())
arr = list(map(int, input().split()))

min_pq = []
max_pq = []

for i, elem in enumerate(arr):
    if i % 2 == 0:
        heappush(min_pq, elem)
    else:
        heappush(max_pq, -elem)
    if max_pq and -max_pq[0] > min_pq[0]:
        a = heappop(min_pq)
        b = -heappop(max_pq)
        heappush(min_pq, b)
        heappush(max_pq, -a)
    if i % 2 == 0:
        print(min_pq[0], end=' ')