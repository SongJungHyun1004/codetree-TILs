n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
prefix = [0]*(n+1)
for i in range(1, n):
    prefix[i] = prefix[i-1]+arr[i]
mx = 0
for i in range(1, n):
    for j in range(i, n):
        if (prefix[j]-prefix[i-1])%7 == 0:
            mx = max(mx, j-i+1)
print(mx)