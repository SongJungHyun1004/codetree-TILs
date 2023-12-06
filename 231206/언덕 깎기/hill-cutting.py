n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
mn_cost = float('inf')
for i in range(n):
    for j in range(i, n):
        if arr[j]-arr[i] > 17:
            continue
        left = arr[0:i]
        right = arr[j+1:n]
        cost = 0
        for l in left:
            x = arr[i] - l
            cost += x*x
        for r in right:
            x = r - arr[j]
            cost += x*x
        mn_cost = min(mn_cost, cost)
print(mn_cost)