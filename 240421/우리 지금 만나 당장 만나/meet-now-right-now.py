import math

n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

def isPossible(mid):
    max_pos = x[0]-v[0]*mid
    min_pos = x[0]+v[0]*mid
    for xi, vi in zip(x, v):
        max_pos = max(max_pos, xi - mid * vi)
        min_pos = min(min_pos, xi + mid * vi)
    return max_pos <= min_pos

def binary_search():
    left = 0
    right = 1000000000
    mn = right
    for _ in range(100):
        mid = (left + right) / 2
        if isPossible(mid):
            right = mid
            mn = min(mn, mid)
        else:
            left = mid
    return format(mn, '.4f')

print(binary_search())