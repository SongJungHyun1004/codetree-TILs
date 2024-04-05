n, k = map(int, input().split())
arr = []
for _ in range(n):
    val, point = map(int, input().split())
    arr.append((point, val))
arr = sorted(arr)
mx = 0
j = 0
summation = 0
for i in range(n):
    while j < n and arr[j][0] - arr[i][0] <= 2*k:
        summation += arr[j][1]
        j += 1
    mx = max(mx, summation)
    summation -= arr[i][1]
print(mx)