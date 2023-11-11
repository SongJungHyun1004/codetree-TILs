n, k = map(int, input().split())
arr = [0]*101
for _ in range(n):
    x, p = map(int, input().split())
    arr[p] += x
mx = float('-inf')
for c in range(100):
    mx = max(mx, sum(arr[max(0, c-k):min(101, c+k+1)]))
print(mx)