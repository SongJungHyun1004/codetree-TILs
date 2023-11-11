n, k = map(int, input().split())
arr = [0]*101
for _ in range(n):
    x, p = map(int, input().split())
    arr[p] = x
mx = float('-inf')
for c in range(k, 101-k+1):
    mx = max(mx, sum(arr[c-k:c+k+1]))
print(mx)