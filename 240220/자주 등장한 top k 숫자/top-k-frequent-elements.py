from collections import Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))
counter = Counter(arr)
counter = sorted(counter.items(), key=lambda x:(x[1],x[0]), reverse=True)
for i, _ in counter[:k]:
    print(i, end=' ')