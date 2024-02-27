n, t = map(int, input().split())
arr = list(map(int, input().split()))
mx = 0
cnt = 0
while arr:
    if arr.pop(0) > t:
        cnt += 1
        mx = max(mx, cnt)
    else:
        cnt = 0
print(mx)