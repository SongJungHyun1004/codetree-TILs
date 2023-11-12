n = int(input())
lst = []
for _ in range(n):
    p, x = input().split()
    lst.append((int(p), x))
lst = sorted(lst)
mx = float('-inf')
for i in range(n):
    for j in range(i, n):
        tmp = [v[1] for v in lst[i:j+1]]
        if all(v == 'G' for v in tmp)  or all(v == 'H' for v in tmp) == 'H' or tmp.count('G') == tmp.count('H'):
            dist = lst[j][0] - lst[i][0]
            mx = max(mx, dist)
print(mx)