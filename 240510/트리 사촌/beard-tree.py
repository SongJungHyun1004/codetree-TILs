import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
root = arr[0]
tmp = []
i, pre = 1, -1
lst = []
while i < n:
    if arr[i]-pre == 1:
        lst.append(arr[i])
    else:
        if lst:
            tmp.append(lst)
        lst = [arr[i]]
    pre = arr[i]
    i += 1
if lst:
    tmp.append(lst) 

tree = defaultdict(list)
parent = {}
noChild = 0
for lst in tmp:
    for x in lst:
        parent[x] = arr[noChild]
    tree[arr[noChild]] = lst
    noChild += 1

p = parent[k]
if p in parent:
    cnt = 0
    for pp in tree[parent[p]]:
        if pp == p:
            continue
        cnt += len(tree[pp])
    print(cnt)
else:
    print(0)