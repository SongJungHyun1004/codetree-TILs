import math
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
info = list(zip(x, v))
info.sort()

def isPossible(mid):
    first = info[0][0]
    last = info[-1][0]
    for p in range(first, last+1):
        mx = -1
        for x, v in info:
            time = abs(x-p)/v
            mx = max(mx, time)
        if mx <= mid:
            return True
    return False

def binary_search():
    left = 0.00000
    right = 1000000000.00000
    mn = right
    i = 0
    while left <= right:
        if i == 30:
            break
        mid = (left+right)//2
        if isPossible(mid):
            right = mid - 1
            mn = min(mn, mid)
        else:
            left = mid + 1
        i += 1
    return format(mn, '.4f')

print(binary_search())