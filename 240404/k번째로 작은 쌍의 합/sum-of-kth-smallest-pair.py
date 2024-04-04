from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))
pq = []
for elem1 in arr1:
    heappush(pq, elem1 + arr2[0])
i, j = 0, 1
while pq and k:
    v = heappop(pq)
    if k == 1:
        break
    heappush(pq, arr1[i]+arr2[j])
    i += 1
    if i == n:
        i = 0; j += 1
    k -= 1
print(v)