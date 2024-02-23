n, k = map(int, input().split())
last_p = 0
lst = []
for _ in range(n):
    m, d = input().split()
    m = int(m)
    if d == 'R':
        s = last_p
        e = last_p + m
        last_p = e
    else:
        e = last_p
        s = last_p - m
        last_p = s
    lst.append((s, +1))
    lst.append((e, -1))
lst = sorted(lst, key=lambda x:(x[0], -x[1]))

pre_cnt = 0
cnt = 0
length = 0
for p, v in lst:
    if v == +1:
        cnt += 1
        if cnt >= k and pre_cnt < k:
            pre_s = p
    else:
        cnt -= 1
        if pre_cnt >= k and cnt < k:
            length += p - pre_s
    pre_cnt = cnt
print(length)