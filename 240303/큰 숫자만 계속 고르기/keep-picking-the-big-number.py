import heapq as hq
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = [-i for i in arr]
hq.heapify(arr)
for _ in range(m):
    mx = hq.heappop(arr)
    hq.heappush(arr, mx+1)
print(-arr[0])