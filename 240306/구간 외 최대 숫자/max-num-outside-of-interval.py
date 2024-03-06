n, q = map(int, input().split())
arr = [0]+list(map(int, input().split()))
L = [0]*(n+1)
R = [0]*(n+2)
for i in range(1, n+1):
    L[i] = max(L[i-1], arr[i])
for i in range(n, 0, -1):
    R[i] = max(R[i+1], arr[i])
for _ in range(q):
    a, b = map(int, input().split())
    print(max(L[a-1], R[b+1]))