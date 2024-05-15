import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1]
pq = []
heappush(pq, arr[0])
heappush(pq, arr[1])
mx = arr[0]
for k in range(2, n):
    heappush(pq, arr[k])
    tmp = heappop(pq)
    avg = sum(pq)/len(pq)
    mx = max(mx, avg)
    heappush(pq, tmp)

print(f'{mx:.2f}')