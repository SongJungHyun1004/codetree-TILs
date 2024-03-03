import heapq as hq
n = int(input())
arr = list(map(int, input().split()))
min_pq = []
for elem in arr:
    hq.heappush(min_pq, elem)
    if len(min_pq) < 3:
        print(-1)
    else:
        one = hq.heappop(min_pq)
        two = hq.heappop(min_pq)
        three = hq.heappop(min_pq)
        print(one*two*three)
        hq.heappush(min_pq, one)
        hq.heappush(min_pq, two)
        hq.heappush(min_pq, three)