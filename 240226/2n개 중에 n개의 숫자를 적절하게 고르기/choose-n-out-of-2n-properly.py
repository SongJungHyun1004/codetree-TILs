n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)

num = []
selected = [False]*len(arr)
mn = float('inf')
def combi(idx, last):
    global mn
    if idx == n:
        mn = min(mn, abs(total-sum(num)*2))
        return
    for i in range(last, len(arr)):
        if not selected[i]:
            num.append(arr[i])
            selected[i] = True
            combi(idx+1, i)
            num.pop()
            selected[i] = False
combi(0, 0)
print(mn)