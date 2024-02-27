n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sum(arr[a1:a2+1]))