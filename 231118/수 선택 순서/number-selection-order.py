from collections import deque
n, x = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(arr)
cnt = 0
while True:
    v = q.popleft()
    x -= 1
    if v > max(q):
        cnt += 1
        if x == -1:
            break
    else:
        q.append(v)
        if x == -1:
            x = len(q)-1
print(cnt)