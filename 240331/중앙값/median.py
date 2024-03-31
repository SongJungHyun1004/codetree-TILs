import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    min_pq = []
    max_pq = []
    for i, elem in enumerate(arr):
        if i%2 == 0:
            heappush(min_pq, elem)
        else:
            heappush(max_pq, -elem)
        if max_pq and min_pq[0] < -max_pq[0]:
            a = heappop(min_pq)
            b = -heappop(max_pq)
            heappush(max_pq, -a)
            heappush(min_pq, b)
        if i%2 == 0:
            print(min_pq[0], end=' ')
    print()