n = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0
for k in range(arr[0], arr[-1]+1):
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] - k == k - arr[i]:
                cnt += 1 
print(cnt)