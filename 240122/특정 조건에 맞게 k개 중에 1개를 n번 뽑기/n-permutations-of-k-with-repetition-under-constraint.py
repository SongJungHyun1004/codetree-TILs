k, n = map(int, input().split())

num = []
def choose(i):
    if i > n:
        print(*num)
        return
    for nn in range(1, k+1):
        if i < 3 or not(nn == num[i-2] and nn == num[i-3]):
            num.append(nn)
            choose(i+1)
            num.pop()

choose(1)