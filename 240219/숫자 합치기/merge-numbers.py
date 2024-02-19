n = int(input())
arr = list(map(int, input().split()))
cost = 0
while len(arr) > 1:
    arr = sorted(arr)
    v = arr[0]+arr[1]
    cost += v
    arr.pop(0)
    arr.pop(0)
    arr.append(v)
print(cost)