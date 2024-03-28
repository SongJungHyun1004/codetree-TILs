from heapq import heappush
n = int(input())
arr = list(map(int, input().split()))
pq = []
heappush(pq, arr[n-1])
summation = pq[0]
mx = 0
for k in range(n-2, 0, -1):
    heappush(pq, arr[k])
    summation += arr[k]
    avg = (summation-pq[0]) / (n-k-1)
    mx = max(mx, avg)

print('%.2f' % mx)