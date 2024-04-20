n, k, b = map(int, input().split())
arr = [0]*(n+1)
for _ in range(b):
    arr[int(input())] = 1
prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+arr[i]
mn = float('inf')
for i in range(1, n-k+2):
    mn = min(mn, prefix[i+k-1]-prefix[i-1])
print(mn)