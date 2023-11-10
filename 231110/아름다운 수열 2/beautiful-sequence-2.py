n, m = map(int, input().split())
a = list(input().split())
b = list(input().split())
cnt = 0
for i in range(n-m+1):
    sub = a[i:i+m]
    if sorted(sub) == sorted(b):
        cnt+= 1
print(cnt)