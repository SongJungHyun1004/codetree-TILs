n = int(input())

visited = [False]*(n+1)
num = []
def choose(i):
    if i > n:
        print(*num)
        return
    for nn in range(1, n+1):
        if visited[nn]:
            continue
        num.append(nn)
        visited[nn] = True
        choose(i+1)
        num.pop()
        visited[nn] = False
choose(1)