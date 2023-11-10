n, k = map(int, input().split())
arr = [0]*(10001)
for _ in range(n):
    x, gh = input().split()
    x = int(x)
    if gh == 'G':
        arr[x] = 1
    else:
        arr[x] = 2
mx = float('-inf')
for i in range(1, 10002-k):
    mx = max(mx, sum(arr[i:i+k+1]))
print(mx)