n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = float('inf')
summation = 0
j = 0
for i in range(n):
    while summation < s and j < n:
        summation += arr[j]
        j += 1
    if summation >= s:
        ans = min(ans, j - i)
    summation -= arr[i]
print(-1) if ans == float('inf') else print(ans)