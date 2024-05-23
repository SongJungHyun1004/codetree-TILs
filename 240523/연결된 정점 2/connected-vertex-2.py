import sys
input = sys.stdin.readline

n = int(input())
uf = [[i, 1] for i in range(10**5+1)]
def find(x):
    if x == uf[x][0]:
        return x
    return find(uf[x][0])

def union(a, b):
    x = find(a)
    y = find(b)
    if x != y:
        uf[x][0] = y
        uf[y][1] += uf[x][1]

for _ in range(n):
    a, b = map(int, input().split())
    union(a, b)
    print(find(uf[a][1]))