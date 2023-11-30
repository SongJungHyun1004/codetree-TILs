n, m = map(int, input().split())
arr = list(map(int, input().split()))
mx = float('-inf')
for s in range(n):
    move = 0
    p = arr[s]
    summation = 0
    while move < m:
        summation += arr[p-1]
        p = arr[p-1]
        move += 1
    mx = max(mx, summation)
print(mx)