import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dots = []
for _ in range(n):
    dots.append(int(input()))
dots = sorted(dots)

def isPossible(mid):
    pre = dots[0]
    cnt = 1
    for nxt in dots[1:]:
        if nxt - pre >= mid:
            cnt += 1
            pre = nxt
    return cnt >= m

def binary_search():
    left = 1
    right = 10**9
    mx = left
    while left <= right:
        mid = (left+right)//2
        if isPossible(mid):
            left = mid + 1
            mx = max(mx, mid)
        else:
            right = mid - 1
    return mx
print(binary_search())