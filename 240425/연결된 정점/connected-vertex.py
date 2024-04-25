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
        if X < Y:
            X, Y = Y, X
        uf[X][0] = Y
        tmp = uf[X][1]+uf[Y][1]
        uf[X][1] = tmp
        uf[Y][1] = tmp
    
for _ in range(m):
    command = list(input().split())
    a = int(command[1])
    if command[0] == 'x':
        b = int(command[2])
        union(a, b)
    elif command[0] == 'y':
        print(uf[find(a)][1])