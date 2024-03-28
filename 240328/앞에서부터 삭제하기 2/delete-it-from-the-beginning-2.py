n = int(input())
arr = [0] + list(map(int, input().split()))

# 왼쪽에서부터 누적합
prefix = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i]

# 오른쪽에서부터 최소값
temp = 10_001
postfix = [0 for _ in range(n+1)]
for i in range(n, -1, -1):
    postfix[i] = min(temp, arr[i])
    temp = postfix[i]

total = sum(arr)
mx = 0
for k in range(1, n-1):
    summation = total - prefix[k] - postfix[k+1]
    avg = summation / (n-k-1)
    mx = max(mx, avg)

print('%.2f' % mx)