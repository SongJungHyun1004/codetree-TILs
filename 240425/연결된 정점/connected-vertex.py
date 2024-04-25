import sys
input = sys.stdin.readline
n, m = map(int, input().split())
uf = [[i, 1] for i in range(n+1)] # 부모, 길이

def find(x):
    if uf[x][0] == x:
        return x
    uf[x][0] = find(uf[x][0])
    return uf[x][0]

def union(x, y):
    X = find(x)
    Y = find(y)
    if X != Y:
        uf[x][0] = y
        uf[x][1] += 1
        uf[y][1] += 1
    
for _ in range(m):
    command = list(input().split())
    a = int(command[1])
    if command[0] == 'x':
        b = int(command[2])
        union(a, b)
    elif command[0] == 'y':
        print(uf[find(a)][1])