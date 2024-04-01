import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cost = []
for _ in range(m):
    cost.append(int(input()))

def isPossible(mid):
    cnt = 0
    for time in cost:
        cnt += mid//time
    return cnt >= n

def binary_search():
    left = 1
    right = 10**9
    mn = right
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            right = mid - 1
            mn = min(mn, mid)
        else:
            left = mid + 1
    return mn

print(binary_search())