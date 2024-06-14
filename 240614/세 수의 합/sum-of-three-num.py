n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        s = arr[i]+arr[j]
        if k-s in dic:
            cnt += dic[k-s]
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1
print(cnt)