n = int(input())

num = []
cnt = 0

def isBeautiful(num):
    idx = 0
    while idx < n:
        if idx+num[idx]-1 >= n:
            return False
        for i in range(idx, idx+num[idx]):
            if num[i] != num[idx]:
                return False
        idx += num[idx]
    return True

def choose(i):
    global cnt
    if i == n:
        if isBeautiful(num):
            cnt += 1
        return
    for nn in range(1, 5):
        num.append(nn)
        choose(i+1)
        num.pop()

choose(0)
print(cnt)