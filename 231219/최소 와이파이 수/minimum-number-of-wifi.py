n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
i = 0
while i < len(arr):
    if arr[i]:
        i += 2*m+1
        cnt += 1
    else:
        i += 1
print(cnt)