from collections import deque
n, x = map(int, input().split())
arr = list(enumerate(list(map(int, input().split()))))
q = deque(arr)
cnt = 0
while True:
    p, v = q[0]
    if q.index(max(q)) == 0:
        q.popleft()
        cnt += 1
        if x == p:
            break
    else:
        q.rotate(-1)
print(cnt)