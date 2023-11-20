from itertools import permutations
k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(list(map(int, input().split())))

lst = [i for i in range(1, n+1)]
perm = list(permutations(lst, 2))
count = 0
for i, j in perm:
    cnt = 0
    for a in arr:
        if a.index(i) < a.index(j):
            cnt += 1
    if cnt == k:
        count += 1
print(count)