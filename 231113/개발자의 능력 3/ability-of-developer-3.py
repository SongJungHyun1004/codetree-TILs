dev = list(map(int, input().split()))
mn = float('inf')
def get_diff(i, j, k):
    sum1 = dev[i]+dev[j]+dev[k]
    sum2 = sum(dev) - sum1
    return abs(sum1 - sum2)

for i in range(len(dev)):
    for j in range(i+1, len(dev)):
        for k in range(j+1, len(dev)):
            mn = min(mn, get_diff(i, j, k))
print(mn)