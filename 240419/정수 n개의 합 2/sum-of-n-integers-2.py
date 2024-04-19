import sys
input = sys.stdin.readline
MIN = -sys.maxsize
n, k = map(int, input().split())
arr = [0]+list(map(int, input().split()))
prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i]

mx = MIN
for i in range(n-k):
    mx = max(mx, prefix[i+k]-prefix[i])
print(mx)