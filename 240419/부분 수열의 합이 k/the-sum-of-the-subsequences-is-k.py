n, k = map(int, input().split())
arr = [0]+list(map(int, input().split()))
prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+arr[i]

cnt = 0
for s in range(1, n+1):
    for e in range(s, n+1):
        if prefix[e]-prefix[s-1] == k:
            cnt += 1
print(cnt)