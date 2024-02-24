n, m = map(int, input().split())
num = []
selected = [False]*n
arr = [i+1 for i in range(n)]
def combi(idx, last):
    if idx == m:
        print(*num)
        return
    for i in range(last, n):
        if not selected[i]:
            num.append(arr[i])
            selected[i] = True
            combi(idx+1, i)
            num.pop()
            selected[i] = False
combi(0, 0)