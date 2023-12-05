n = int(input())
arr = list(map(int, input().split()))
lst = []
for first in range(1, n+1):
    lst = [first]
    i = 1
    while i < n:
        for nxt in range(1, n+1):
            if nxt in lst or lst[-1]+nxt != arr[i-1]:
                continue
            lst.append(nxt)
            break
        if len(lst) != i+1:
            break
        i += 1
    if len(lst) == n:
        print(*lst)
        break