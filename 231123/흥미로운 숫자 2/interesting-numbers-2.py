x, y = map(int, input().split())

def isInteresting(n):
    lst = list(map(int, str(n)))
    if len(set(lst)) != 2:
        return False
    lst = sorted(lst)
    if lst[0] == lst[1] and lst[-1] == lst[-2]:
        return False
    return True

cnt = 0
for i in range(x, y+1):
    if isInteresting(i):
        cnt += 1
print(cnt)