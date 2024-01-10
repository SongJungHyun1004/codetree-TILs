from itertools import combinations
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def isOverlapped(box1, box2):
    si,sj,ei,ej = box1
    si2,sj2,ei2,ej2 = box2
    if ei <= si2 or ej <= sj2:
        return False
    return True

def get_summation(box1, box2):
    summation = 0
    si,sj,ei,ej = box1
    si2,sj2,ei2,ej2 = box2
    for i in range(si, ei):
        for j in range(sj, ej):
            summation += grid[i][j]
    for i in range(si2, ei2):
        for j in range(sj2, ej2):
            summation += grid[i][j]
    return summation

ans = float('-inf')
lst = []
for i in range(n+1):
    for j in range(m+1):
        for k in range(i+1, n+1):
            for l in range(j+1, m+1):
                lst.append((i,j,k,l))
lst2 = []
lst2 += list(combinations(lst, 2))
for box1, box2 in lst2:
    if not isOverlapped(box1, box2):
        # print(box1, box2)
        hap = get_summation(box1, box2)
        ans = max(ans, hap)
print(ans)