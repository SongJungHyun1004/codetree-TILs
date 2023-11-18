from collections import deque
n, x = map(int, input().split())
arr = list(enumerate(list(map(int, input().split()))))
for i in range(n):
    idx, value = arr[i]
    arr[i] = (value, idx)
q = deque(arr)
cnt = 0
while True:
    v, p = q[0]
    if max(q)[0] == v:
        q.popleft()
        cnt += 1
        if x == p:
            break
    else:
        q.rotate(-1)
print(cnt)