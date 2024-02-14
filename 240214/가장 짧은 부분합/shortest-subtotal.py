n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = float('inf')
for i in range(n):
    summation = 0
    for j in range(i, n):
        summation += arr[j]
        if summation >= s:
            ans = min(ans, j-i+1)
            break
print(-1) if ans == float('inf') else print(ans)