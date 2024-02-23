n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, +1))
    lst.append((e, -1))
lst = sorted(lst, key=lambda x:(x[0], -x[1]))
pre_cnt = 0
cnt = 0
length = []
for p, v in lst:
    if v == +1:
        cnt += 1
        if cnt >= 1 and pre_cnt == 0:
            pre_s = p
    else:
        cnt -= 1
        if pre_cnt >= 1 and cnt == 0:
            length.append(p-pre_s)
    pre_cnt = cnt
print(max(length))