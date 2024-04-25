import sys
input = sys.stdin.readline
n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    X = find(x)
    Y = find(y)
    if X != Y:
        uf[x] = y
    
for _ in range(m):
    command = list(input().split())
    a = int(command[1])
    if command[0] == 'x':
        b = int(command[2])
        union(a, b)
    elif command[0] == 'y':
        cnt = 0
        for i in range(1, n+1):
            if find(a) == find(i):
                cnt += 1
        print(cnt)