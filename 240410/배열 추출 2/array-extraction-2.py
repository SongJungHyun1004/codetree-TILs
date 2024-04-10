from heapq import heappush, heappop

n = int(input())
pq = []
for _ in range(n):
    x = int(input())
    if x < 0:
        heappush(pq, (-x, -1))
    elif x > 0:
        heappush(pq, (x, 1))
    else:
        if pq:
            x, sign = heappop(pq)
            print(x*sign)
        else:
            print(0)