n, k = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if k-arr[i]-arr[j] in dic:
            cnt += dic[k-arr[i]-arr[j]]
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1
print(cnt)