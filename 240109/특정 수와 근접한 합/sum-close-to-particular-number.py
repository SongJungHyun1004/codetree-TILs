n, s = map(int, input().split())
arr = list(map(int, input().split()))
summation = sum(arr)
mn = float('inf')
for i in range(n):
    for j in range(i+1, n):
        hap = summation - arr[i] - arr[j]
        mn = min(mn, abs(s-hap))
print(mn)