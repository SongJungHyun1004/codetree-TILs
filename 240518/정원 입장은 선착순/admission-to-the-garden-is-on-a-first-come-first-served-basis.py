import sys
input = sys.stdin.readline
MAX = sys.maxsize
from heapq import heappush, heappop

n = int(input())
info = []
for i in range(n):
    a, t = map(int, input().split())
    info.append((a, i, t))
info.append((MAX, n, 0))
info.sort()

pq = []
cur = 0
mx = 0
for a, num, t in info:
    while pq and a > cur:
        _, wait_a, wait_t = heappop(pq)
        mx = max(mx, cur-wait_a)
        cur += wait_t
    if a > cur:
        cur = a + t
    else:
        heappush(pq, (num, a, t))

print(mx)