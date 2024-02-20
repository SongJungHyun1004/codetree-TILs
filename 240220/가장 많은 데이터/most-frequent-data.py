from collections import Counter
n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr = Counter(arr)
mx = 0
for v in arr.values():
    mx = max(mx, v)
print(mx)