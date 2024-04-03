import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = map(int, input().split())
    for x in range(a, b+1):
        lines.append(x)
lines = sorted(lines)

def isPossible(mid):
    pre = lines[0]
    cnt = 1
    for nxt in lines[1:]:
        if nxt - pre >= mid:
            cnt += 1
            pre = nxt
    return cnt >= n

def binary_search():
    left = 1
    right = 10**18
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