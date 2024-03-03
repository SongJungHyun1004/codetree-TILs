import heapq as hq
n, m = map(int, input().split())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    hq.heappush(pos, (x+y, x, y))

for _ in range(m):
    v, x, y = hq.heappop(pos)
    hq.heappush(pos, (v+4, x+2, y+2))
_, x, y = pos[0]
print(x, y)