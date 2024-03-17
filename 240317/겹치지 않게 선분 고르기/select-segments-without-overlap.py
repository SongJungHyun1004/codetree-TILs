n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, e))
lst = sorted(lst)
selected = []

def is_ok(selected):
    for i in range(len(selected)):
        for j in range(i+1, len(selected)):
            s1, e1 = lst[selected[i]]
            s2, e2 = lst[selected[j]]
            if e1 >= s2:
                return False
    return True

def choose(i):
    global mx
    if i == n:
        if is_ok(selected):
            mx = max(mx, len(selected))
        return
    
    selected.append(i)
    choose(i+1)
    selected.pop()
    choose(i+1)

mx = 1
choose(0)
print(mx)