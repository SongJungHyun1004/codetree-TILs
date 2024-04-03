import sys
input = sys.stdin.readline
INT_MIN = -sys.maxsize
n = int(input())
lines = []
for _ in range(n):
    s, e = map(int, input().split())
    lines.append((s, e))
lines = sorted(lines)

def isPossible(mid):
    cnt = 0
    last = INT_MIN
    for s, e in lines:
        if last + mid <= e:
            cnt += 1
            last = max(s, last+mid)
            if cnt >= n:
                return True
    return cnt >= n
    

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