from collections import Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = Counter(arr)
cnt = 0
for i in arr:
    if k-i in arr:
        cnt += max(arr[i], arr[k-i])
print(cnt//2)