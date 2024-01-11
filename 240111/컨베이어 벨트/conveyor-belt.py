n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = a+b
for _ in range(t):
    arr = [arr[-1]]+arr[:-1]
for i in range(n):
    print(arr[i],end=' ')
print()
for i in range(n,2*n):
    print(arr[i],end=' ')