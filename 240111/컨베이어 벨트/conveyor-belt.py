n, t = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = a+b
for _ in range(t):
    arr = [arr[-1]]+arr[:-1]
print(*arr[:n])
print(*arr[n:])