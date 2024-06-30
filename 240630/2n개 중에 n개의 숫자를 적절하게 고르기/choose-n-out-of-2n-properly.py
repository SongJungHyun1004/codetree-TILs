n = int(input())
arr = list(map(int, input().split()))
visited = [False]*n
total = sum(arr)
num = []
mn = total

def choose(i, cnt):
    global mn
    if i == 2*n:
        if cnt == n:
            mn = min(mn, abs(total-2*sum(num)))
            return
        return
    num.append(arr[i])
    choose(i+1, cnt+1)
    num.pop()
    choose(i+1, cnt)

choose(0, 0)
print(mn)