n = int(input())
arr = sorted(list(map(int, input().split())))
a = arr[:n]
b = arr[n:]
mn = float('inf')
for i in range(n):
    cha = b[i]-a[i]
    if mn > cha:
        mn = cha
print(mn)