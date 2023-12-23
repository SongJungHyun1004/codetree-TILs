from collections import deque
n = int(input())
dq = deque([i+1 for i in range(n)])
while len(dq) != 1:
    dq.popleft()
    dq.rotate(-1)
print(dq[0])