n, q = map(int, input().split())
pos = sorted(list(map(int, input().split())))
mapper = {}
num = 0
for p in pos:
    mapper[p] = num
    num += 1

for _ in range(q):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        if i in mapper:
            cnt += 1
    print(cnt)