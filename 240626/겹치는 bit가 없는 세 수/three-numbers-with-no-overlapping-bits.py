n = int(input())
arr = list(map(int, input().split()))
mx = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not (arr[i] & arr[j]) and not (arr[k] & arr[j]) and not (arr[i] & arr[k]):
                mx = max(mx, arr[i]+arr[j]+arr[k])
print(mx)