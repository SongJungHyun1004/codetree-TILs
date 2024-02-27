import math
n = int(input())
arr = list(map(int, input().split()))

pre = arr[0]
for i in range(1, n):
    pre = math.lcm(pre, arr[i])
print(pre)