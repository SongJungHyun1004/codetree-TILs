n = int(input())
arr = [i+1 for i in range(n)]
visited = [False]*n
num = []

def choose(i):
    if i == n:
        print(*num)
        return
    for j in range(n):
        if not visited[j]:
            num.append(arr[j])
            visited[j] = True
            choose(i+1)
            num.pop()
            visited[j] = False

choose(0)