n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
summation = 0
j = 0
for i in range(n):
    while j < n and summation < m:
        summation += arr[j]
        j += 1
    if summation == m:
        cnt += 1
    summation -= arr[i]
print(cnt)