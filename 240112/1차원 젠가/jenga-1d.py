n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for _ in range(2):
    s, e = map(int, input().split())
    s-=1;e-=1
    tmp = []
    for i in range(len(arr)):
        if not (s <= i <= e):
            tmp.append(arr[i])
    arr = tmp[:]
print(len(arr))
for i in arr:
    print(i)