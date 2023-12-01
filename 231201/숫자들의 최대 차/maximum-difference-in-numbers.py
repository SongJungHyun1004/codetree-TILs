n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
mx = float('-inf')
for i in range(1, max(arr)+1):
    lst = []
    for a in arr:
        if i <= a <= i+k:
            lst.append(a)
    mx = max(mx, len(lst))
print(mx)