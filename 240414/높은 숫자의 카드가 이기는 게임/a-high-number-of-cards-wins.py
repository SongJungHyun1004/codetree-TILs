from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
B = []
for _ in range(n):
    B.append(int(input()))
total = set([i+1 for i in range(2*n)])
A = list(total-set(B))
heapify(A)
heapify(B)
score = 0
b = heappop(B)
while A:
    a = heappop(A)
    if a > b:
        score += 1
        if B:
            b = heappop(B)
        else:
            break
print(score)