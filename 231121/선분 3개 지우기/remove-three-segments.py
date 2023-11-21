n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
def isOverlapped(i, j, k):
    lst = [0]*101
    for ii in range(n):
        if ii == i or ii == j or ii == k:
            continue
        a, b = lines[ii]
        for jj in range(a, b+1):
            lst[jj] += 1
    for l in lst:
        if l > 1:
            return True
    return False

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not isOverlapped(i, j, k):
                cnt += 1
print(cnt)