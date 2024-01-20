k, n = map(int, input().split())
num = []
def choose(i):
    if i > n:
        print(*num)
        return
    for kk in range(1, k+1):
        num.append(kk)
        choose(i+1)
        num.pop()
choose(1)