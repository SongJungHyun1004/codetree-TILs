n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))
mn = float('inf')
for i in range(arr[0], arr[-1]-k+1):
    tmp = arr[:]
    cost = 0
    for j in tmp:
        if j < i:
            cost += i-j
        elif j > i+k:
            cost += j-(i+k)
    mn = min(mn, cost)
print(mn)