import sys
input = sys.stdin.readline

from heapq import heappush, heappop
t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    min_pq = []
    max_pq = []
    for i in range(m):
        if i%2==0:
            heappush(max_pq, -arr[i])
        else:
            heappush(min_pq, arr[i])
        if i > 0 and -max_pq[0] > min_pq[0]:
            a = -heappop(max_pq)
            b = heappop(min_pq)
            heappush(max_pq, -b)
            heappush(min_pq, a)
        if i%2==0:
            print(-max_pq[0], end=' ')
    print()