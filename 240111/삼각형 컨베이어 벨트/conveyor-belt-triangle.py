n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
arr = a+b+c
for _ in range(t):
    arr = [arr[-1]]+arr[:-1]
print(*arr[:n])
print(*arr[n:2*n])
print(*arr[2*n:])