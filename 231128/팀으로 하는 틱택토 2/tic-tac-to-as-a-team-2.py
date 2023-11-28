ttt = [
    list(input())
    for _ in range(3)
]
cnt = set()
for i in range(3):
    if len(set(ttt[i])) == 2:
        cnt.add(tuple(sorted(ttt[i])))
    tmp = [ttt[j][i] for j in range(3)]
    if len(set(tmp)) == 2:
        cnt.add(tuple(sorted(tmp)))
tmp2 = [ttt[0][0], ttt[1][1], ttt[2][2]]
tmp3 = [ttt[0][2], ttt[1][1], ttt[2][0]]
if len(set(tmp2)) == 2:
    cnt.add(tuple(sorted(tmp2)))
if len(set(tmp3)) == 2:
    cnt.add(tuple(sorted(tmp3)))
print(len(cnt))