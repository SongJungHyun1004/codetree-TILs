n, m = map(int, input().split())
a = [0]
b = [0]

def move(lst, nn):
    dist = 0
    for _ in range(nn):
        v, t = map(int, input().split())
        for _ in range(t):
            dist += v
            lst.append(dist)
move(a, n)
move(b, m)
cnt = 0
if len(b) < len(a):
    a = a[:len(b)]
pre_state = 0 # a,b 같은 상태: 0, a가 큰 상태: 1, b가 큰 상태 2
for i, j in zip(a, b):
    if i > j:
        cur_state = 1
    elif i < j:
        cur_state = 2
    else:
        cur_state = 0
    if pre_state != cur_state:
        cnt += 1
    pre_state = cur_state
print(cnt)