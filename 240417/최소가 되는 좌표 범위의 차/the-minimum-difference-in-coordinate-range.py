from sortedcontainers import SortedSet
import sys
input = sys.stdin.readline
MAX = sys.maxsize
n, d = map(int, input().split())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))
pos = sorted(pos)
mn = MAX
treeset = SortedSet()
j = 0
for i in range(n):
    treeset.add((pos[i][1], pos[i][0]))
    while treeset and treeset[-1][0] - treeset[0][0] >= d:
        mn = min(mn, pos[i][0]-pos[j][0])
        treeset.remove((pos[j][1], pos[j][0]))
        j += 1
print(mn) if mn != MAX else print(-1)