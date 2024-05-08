import sys
input = sys.stdin.readline
from heapq import heappush, heappop
c, n = map(int, input().split())
red = []
black = []
for _ in range(c):
    heappush(red, int(input()))
for _ in range(n):
    a, b = map(int, input().split())
    heappush(black, (b, a))

cnt = 0
while red and black:
    t = heappop(red)
    b, a = heappop(black)
    if a <= t <= b:
        cnt += 1
    if b < t:
        heappush(red, t)
    if a > t:
        heappush(black, (b, a))
print(cnt)