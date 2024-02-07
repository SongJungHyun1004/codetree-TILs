n = int(input())
arr = [1.0]
for _ in range(n):
    arr.append(float(input()))
for i in range(1, n+1):
    arr[i] = arr[i-1]*arr[i]
mx = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        mx = max(mx, arr[j]/arr[i])
print(round(mx, 3))