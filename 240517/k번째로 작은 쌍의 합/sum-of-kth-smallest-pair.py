import sys
input = sys.stdin.readline

from heapq import heappush, heappop

n, m, k = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))

pq = []
for i in range(n):
    heappush(pq, (arr1[i]+arr2[0], i, 0))

for _ in range(k-1):
    _, i, j = heappop(pq)
    if j+1 < m:
        heappush(pq, (arr1[i]+arr2[j+1], i, j+1))

ans, _, _ = heappop(pq)
print(ans)