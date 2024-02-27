n = int(input())
lst = []
for i in range(1, n+1):
    height, weight = map(int, input().split())
    lst.append((height, weight, i))

lst = sorted(lst, key=lambda x: (x[0], -x[1]))

for h, w, i in lst:
    print(h, w, i)