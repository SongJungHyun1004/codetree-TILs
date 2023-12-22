from collections import deque
n, k = map(int, input().split())
lst = []
q = deque([i+1 for i in range(n)])
for _ in range(n):
    q.rotate(-(k-1))
    lst.append(q.popleft())
print(*lst)