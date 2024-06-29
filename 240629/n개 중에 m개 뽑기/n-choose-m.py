n, m = map(int, input().split())
numbers = [i+1 for i in range(n)]
num = []
def choose(i, cnt):
    if i == n:
        if cnt == m:
            print(*num)
        return
    num.append(numbers[i])
    choose(i+1, cnt+1)
    num.pop()
    choose(i+1, cnt)

choose(0, 0)