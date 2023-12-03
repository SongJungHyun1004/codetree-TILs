n = int(input())
arr = list(map(int, input().split()))
cnt = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if i+j != arr[0] or i == j:
            continue
        for k in range(1, n+1):
            if j+k != arr[1] or k == j or k == i:
                continue
            for l in range(1, n+1):
                if k+l != arr[2] or l == k or l== j or l == i:
                    continue
                for m in range(1, n+1):
                    if l+m != arr[3] or m == l or m == k or m == j or m == i:
                        continue
                    cnt.append([i, j, k, l, m])
cnt = sorted(cnt)
print(*cnt[0])