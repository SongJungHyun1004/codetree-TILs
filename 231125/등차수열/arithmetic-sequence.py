n = int(input())
arr = list(map(int, input().split()))

mx = float('-inf')
for k in range(min(arr), max(arr)+1):
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] - k == k - arr[i]:
                cnt += 1
    mx = max(mx, cnt)
print(mx)