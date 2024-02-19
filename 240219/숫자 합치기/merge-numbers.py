import heapq
n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
cost = 0
while len(arr) > 1:
    v = heapq.heappop(arr)+heapq.heappop(arr)
    cost += v
    heapq.heappush(arr, v)
print(cost)