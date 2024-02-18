n = int(input())
arr = list(map(int, input().split()))
mx = float('-inf')
summation = 0
for i in range(n):
    summation += arr[i]
    mx = max(mx, summation)
    if summation < 0:
        summation = 0
print(mx)