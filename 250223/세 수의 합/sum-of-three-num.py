n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
count = {}
ans = 0
for i in range(n):
    for j in range(i+1, n):
        s = arr[i] + arr[j]
        if k-s in count:
            ans += count[k-s]
    if arr[i] in count:
        count[arr[i]] += 1
    else:
        count[arr[i]] = 1

print(ans)