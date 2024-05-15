import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
mx = 0
for k in range(n-3):
    pq = []
    for i in range(k+1, n):
        heappush(pq, arr[i])
    heappop(pq)
    avg = sum(pq)/len(pq)
    mx = max(mx, avg)

print(f'{mx:.2f}')