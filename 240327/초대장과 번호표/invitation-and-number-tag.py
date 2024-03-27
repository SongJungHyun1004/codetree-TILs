from collections import deque
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
groups = sorted(groups, key=lambda x: len(x))
invited = deque([1])
ans = 1
while invited:
    p = invited.popleft()
    for grp in groups:
        grp.discard(p)
        if len(grp) == 1:
            new = grp.pop()
            if new not in invited:
                invited.append(new)
                ans += 1
print(ans)