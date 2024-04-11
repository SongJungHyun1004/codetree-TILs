import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
m = 2*10**9
i = 0; j = n-1
while i < j:
    s = arr[i] + arr[j]
    if s == 0:
        print(0)
        exit(0)
    if s > 0:
        j -= 1
    elif s < 0:
        i += 1
    m = min(m, abs(s))
print(m)