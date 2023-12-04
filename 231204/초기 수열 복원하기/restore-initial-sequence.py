from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
lst = [i for i in range(1, n+1)]
tmp = []
tmp += list(permutations(lst, n))
for i in tmp:
    perm = list(i)
    flag = 1
    for j in range(1, n):
        if perm[j-1] + perm[j] != arr[j-1]:
            flag = 0
            break
    if flag:
        print(*perm)
        break