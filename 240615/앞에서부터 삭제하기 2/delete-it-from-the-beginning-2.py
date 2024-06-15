from heapq import heappush, heappop

n = int(input())
arr = list(map(int, input().split()))
pq = []
heappush(pq, arr[-1])
heappush(pq, arr[-2])
mx = 0
for k in range(n-3, -1, -1):
    mn = heappop(pq)
    avg = sum(pq)/len(pq)
    mx = max(mx, avg)
    heappush(pq, mn)
    heappush(pq, arr[k])
print(f'{mx:.2f}')