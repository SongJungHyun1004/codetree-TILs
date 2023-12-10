n = int(input())
lines = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append((x1, x2))
for i in range(n):
    tmp = [0]*101
    for j in range(n):
        if i == j:
            continue
        for k in range(lines[j][0], lines[j][1]+1):
            tmp[k] += 1
    if n-1 in tmp:
        print("Yes")
        exit(0)
print("No")