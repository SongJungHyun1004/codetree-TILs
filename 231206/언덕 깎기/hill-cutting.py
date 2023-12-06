n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
mn_cost = float('inf')
if arr[-1] < 17:
    print(0)
    exit(0)

for i in range(arr[0], arr[-1]-17+1):
    cost = 0
    for v in arr:
        if not i <= v <= i+17:
            if v < i:
                x = i-v
            if v > i+17:
                x = v-(i+17)
            cost += x*x
    mn_cost = min(mn_cost, cost)
print(mn_cost)