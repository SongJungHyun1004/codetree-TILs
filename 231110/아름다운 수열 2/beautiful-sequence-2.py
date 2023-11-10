from itertools import permutations
n, m = map(int, input().split())
a = list(input().split())
b = list(input().split())
tmp = list(set(list(permutations(b, m))))
cnt = 0
for t in tmp:
    t = ''.join(list(t))
    a = ''.join(a)
    for i in range(len(a)-len(t)+1):
        if t == a[i:i+len(t)]:
            cnt += 1
print(cnt)