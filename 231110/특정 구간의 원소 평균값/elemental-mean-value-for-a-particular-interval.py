n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        sub = arr[i:j+1]
        avg = sum(sub)/len(sub)
        if avg in sub:
            cnt += 1
print(cnt)