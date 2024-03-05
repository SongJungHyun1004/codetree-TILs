n, q = map(int, input().split())
pos = sorted(list(map(int, input().split())))
mapper = {}
num = 0
for p in pos:
    mapper[p] = num
    num += 1

for _ in range(q):
    a, b = map(int, input().split())
    print(mapper[b]-mapper[a]+1)