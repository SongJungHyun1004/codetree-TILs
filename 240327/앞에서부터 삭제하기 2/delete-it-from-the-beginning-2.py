from heapq import heapify, heappush, heappop
n = int(input())
arr = list(map(int, input().split()))
mx = 0
for k in range(1, n-1):
    tmp = arr[k:]
    heapify(tmp)
    heappop(tmp)
    avg = sum(tmp)/len(tmp)
    mx = max(mx, avg)
print('%.2f'%mx)