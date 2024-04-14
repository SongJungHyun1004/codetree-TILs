from heapq import heapify, heappush, heappop
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
B = []
for _ in range(n):
    B.append(int(input()))
total = set([i+1 for i in range(2*n)])
A = list(total-set(B))
heapify(A)
B = deque(B)
score = 0
while A:
    a = heappop(A)
    b = B.popleft()
    if a > b:
        score += 1
print(score)