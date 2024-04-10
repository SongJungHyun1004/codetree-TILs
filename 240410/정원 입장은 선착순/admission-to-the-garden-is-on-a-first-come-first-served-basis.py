from heapq import heappush, heappop
import sys
input = sys.stdin.readline
MAX = 10**4
n = int(input())
pq = []
for i in range(n):
    a, t = map(int, input().split())
    heappush(pq, (a, i, t))

last = 0
mx = 0   
waiting = []
while pq:
    while last > pq[0][0]:
        a, i, t = heappop(pq)
        heappush(waiting, (i, a, t))
        if not pq:
            break
    if not waiting:
        a, _, t = heappop(pq)
        last = a + t
    else:
        _, a, t = heappop(waiting)
        wait = last - a
        mx = max(mx, wait)
        last += t
        if pq and last > pq[0][0]:
            continue
        flag = 0
        while waiting:
            _, a, t = heappop(waiting)
            wait = last - a
            mx = max(mx, wait)
            last += t
            if pq and last > pq[0][0]:
                flag = 1
                break
        if flag:
            continue
print(mx)