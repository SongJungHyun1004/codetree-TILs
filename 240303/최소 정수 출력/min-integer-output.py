import heapq as hq
n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    if x:
        hq.heappush(arr, x)
    else:
        if arr:
            print(hq.heappop(arr))
        else:
            print(0)