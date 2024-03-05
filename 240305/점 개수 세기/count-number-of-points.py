import sys
from sortedcontainers import SortedSet
input = sys.stdin.readline
n, q = map(int, input().split())
pos = SortedSet(list(map(int, input().split())))
mapper = {}
num = 0
for p in pos:
    mapper[p] = num
    num += 1

for _ in range(q):
    a, b = map(int, input().split())
    if pos.bisect_left(a) == len(pos):
        print(0)
    else:
        idx_a = mapper[pos[pos.bisect_left(a)]]
        idx_b = mapper[pos[pos.bisect_right(b)-1]]
        print(idx_b-idx_a+1)