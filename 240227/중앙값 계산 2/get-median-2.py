n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n, 2):
    lst = arr[:i+1]
    lst = sorted(lst)
    print(lst[len(lst)//2], end=' ')