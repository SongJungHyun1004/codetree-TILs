ttt = [
    list(input())
    for _ in range(3)
]
cnt = 0
for i in range(3):
    if len(set(ttt[i])) == 2:
        cnt += 1
    tmp = [ttt[j][i] for j in range(3)]
    if len(set(tmp)) == 2:
        cnt += 1
if len(set([ttt[0][0], ttt[1][1], ttt[2][2]])) == 2:
    cnt += 1
if len(set([ttt[0][2], ttt[1][1], ttt[2][0]])) == 2:
    cnt += 1
print(cnt)