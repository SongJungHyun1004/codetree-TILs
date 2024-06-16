from collections import Counter
n, k = map(int, input().split())
counter = Counter(list(map(int, input().split())))

lst = sorted(counter.items(), key=lambda x:(-x[1], -x[0]))
for i in range(k):
    print(lst[i][0], end=' ')