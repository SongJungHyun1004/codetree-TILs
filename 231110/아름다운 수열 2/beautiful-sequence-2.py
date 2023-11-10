from itertools import permutations
n, m = map(int, input().split())
a = list(input().split())
b = list(input().split())
tmp = list(set(list(permutations(b, m))))
cnt = 0
for t in tmp:
    t = ''.join(list(t))
    if t in ''.join(a):
        cnt += 1
print(cnt)