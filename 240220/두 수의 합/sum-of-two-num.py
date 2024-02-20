n, k = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}
cnt = 0
for i in arr:
    if k-i in dic:
        cnt += dic[k-i]
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(cnt)