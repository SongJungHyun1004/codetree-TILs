n, m = map(int, input().split())
num = []
visited = [False]*(n+1)
def combi(i, last):
    if i == m:
        print(*num)
        return
    for nn in range(last, n+1):
        if not visited[nn]:
            num.append(nn)
            visited[nn] = True
            combi(i+1, nn+1)
            num.pop()
            visited[nn] = False
combi(0, 1)