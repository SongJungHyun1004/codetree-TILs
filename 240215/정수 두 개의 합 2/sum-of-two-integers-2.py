n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
cnt = 0
i, j = 0, n-1
while i < j:
    if arr[i] + arr[j] <= k:
        cnt += j-i
        i += 1
    else:
        j -= 1
print(cnt)