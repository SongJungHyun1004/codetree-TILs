n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = float('inf')
summation = 0
j = 0
for i in range(n):
    while j < n:
        if summation >= s:
            break
        summation += arr[j]
        j+=1
    ans = min(ans, j-i+1)
    summation -= arr[i]
print(-1) if ans == float('inf') else print(ans)