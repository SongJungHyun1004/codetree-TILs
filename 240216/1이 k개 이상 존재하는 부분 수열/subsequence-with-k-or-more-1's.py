import sys
INT_MAX = sys.maxsize
n, k = map(int, input().split())
arr = list(map(int, input().split()))
mn = INT_MAX
cnt_one = 0
i, j = 0, 0
for i in range(n):
    while j < n and cnt_one < k:
        if arr[j] == 1:
            cnt_one += 1
        j += 1
    if cnt_one < k:
        break
    mn = min(mn, j-i)
    if arr[i] == 1:
        cnt_one -= 1
if mn == INT_MAX:
    print(-1)
else:
    print(mn)