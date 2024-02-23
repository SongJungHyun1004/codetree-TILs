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
lst = sorted(lst)

cnt = 0
length = 0
for i, (p, v) in enumerate(lst):
    if cnt >= k:
        pre_p, _ = lst[i-1]
        length += p - pre_p
    cnt += v
print(length)