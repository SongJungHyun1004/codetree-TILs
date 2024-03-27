n, g = map(int, input().split())
groups = [
    set()
    for _ in range(g)
]
info = [
    list(map(int, input().split()))
    for _ in range(g)
]
for i in range(g):
    for j in range(1, len(info[i])):
        groups[i].add(info[i][j])
groups = sorted(groups)
invited = set()
invited.add(1)
for grp in groups:
    if len(grp-invited) == 1:
        invited = invited.union(grp)
print(len(invited))