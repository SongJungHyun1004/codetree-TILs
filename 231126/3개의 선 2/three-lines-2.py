n = int(input())
MAX = 10
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))
def canPassAll():
    xys = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    for i in range(MAX+1):
        for j in range(MAX+1):
            for k in range(MAX+1):
                for xy1, xy2, xy3 in xys:
                    ans = 1
                    for p in lst:
                        if p[xy1] == i or p[xy2] == j or p[xy3] == k:
                            continue
                        ans = 0
                    if ans:
                        return 1
    return 0
print(canPassAll())