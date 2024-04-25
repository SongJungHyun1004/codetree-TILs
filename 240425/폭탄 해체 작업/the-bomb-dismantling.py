from heapq import heappush, heappop
n = int(input())
bombs = []
for _ in range(n):
    score, time = map(int, input().split())
    bombs.append((score, time))
bombs.sort(key = lambda x: x[1])
m = bombs[-1][1]
time_lst = [[] for _ in range(m+1)]
for s, t in bombs:
    time_lst[t].append(s)

ans = 0
pq = []
for t in range(m, 0, -1):
    for s in time_lst[t]:
        heappush(pq, -s)
    if pq:
        ans += -heappop(pq)
print(ans)