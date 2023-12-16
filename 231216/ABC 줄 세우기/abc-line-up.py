n = int(input())
arr = input().split()
cnt = 0
for i in range(n):
    idx = arr.index(chr(ord('A')+i))
    for j in range(idx, i, -1):
        arr[j], arr[j-1] = arr[j-1], arr[j]
        cnt += 1
print(cnt)