import sys
input = sys.stdin.readline
m = int(input())
parent = {}

def find(x):
    if x not in parent:
        return x
    return find(parent[x])

def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        parent[y] = x

node = set()
for _ in range(m):
    a, b = map(int, input().split())
    node.add(a)
    node.add(b)
    if b in parent:
        print(0)
        exit(0)
    else:
        if find(a) == find(b):
            print(0)
            exit(0)
        else:
            union(a, b)

root = 0
for x in list(node):
    if x not in parent:
        root += 1

if root == 1:
    print(1)
else:
    print(0)