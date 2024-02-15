n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 0
j = 1
for i in range(n-1):
    if i==j:
        j += 1
    while j < n and arr[i] + arr[j] <= k:
        j += 1
        cnt += 1
print(cnt)