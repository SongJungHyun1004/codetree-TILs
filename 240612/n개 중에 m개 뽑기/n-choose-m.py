n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
num = []
def combi(i, cnt):
    if i == n:
        if cnt == m:
            print(*num)
        return
    num.append(arr[i])
    combi(i+1, cnt+1)
    num.pop()
    combi(i+1, cnt)
combi(0, 0)