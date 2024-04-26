import sys
input = sys.stdin.readline

n, q = map(int, input().split())
pos = sorted(list(map(int, input().split())))
MAX = 10**6
prefix = [0]*(MAX+1)
for p in pos:
    prefix[p] = 1
for i in range(MAX+1):
    prefix[i] += prefix[i-1]

for _ in range(q):
    a, b = map(int, input().split())
    if a == 0:
        print(prefix[b])
    else:
        print(prefix[b]-prefix[a-1])