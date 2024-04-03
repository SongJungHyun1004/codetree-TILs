import sys
input = sys.stdin.readline
INT_MIN = -sys.maxsize
n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = map(int, input().split())
    lines.append((a, b))
lines = sorted(lines)

def isPossible(mid):
    cnt = 0
    last = INT_MIN
    for a, b in lines:
        while last + mid <= b:
            cnt += 1
            last = max(a, last + mid)
            if cnt >= n:
                return True
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