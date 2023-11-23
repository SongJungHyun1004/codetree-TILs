n, c, g, h = map(int, input().split())
lst1, lst2 = [], []
for _ in range(n):
    ta, tb = map(int, input().split())
    lst1.append(ta)
    lst2.append(tb)
def get_workload(i, ta, tb):
    if i < ta:
        return c
    elif i <= tb:
        return g
    else:
        return h
mx = float('-inf')
for i in range(min(lst1), max(lst2)+2):
    workload = 0
    for ta, tb in zip(lst1, lst2):
        workload += get_workload(i, ta, tb)
    mx = max(mx, workload)
print(mx)