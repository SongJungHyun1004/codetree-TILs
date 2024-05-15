import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
pq = []
heappush(pq, arr[-1])
summation = pq[0]
mx = 0
for k in range(n-2, 0, -1):
    heappush(pq, arr[k])
    summation += arr[k]
    avg = (summation-pq[0])/(len(pq)-1)
    mx = max(mx, avg)

print(f'{mx:.2f}')