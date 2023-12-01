n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
mx = float('-inf')
for i in range(1, 10000):
    lst = []
    for a in arr:
        if i <= a <= i+3:
            lst.append(a)
    mx = max(mx, len(lst))
print(mx)