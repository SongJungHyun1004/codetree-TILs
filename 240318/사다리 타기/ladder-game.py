n, m = map(int, input().split())
init_info = []
for _ in range(m):
    a, b = map(int, input().split())
    init_info.append((a, b))
    
def make_ladder(info):
    ladder = [
        [0]*(n+1)
        for _ in range(16)
    ]
    for a, b in info:
        ladder[b][a] = 1
        ladder[b][a+1] = -1
    return ladder

def simulate(ladder):
    result = []
    for num in range(1, n+1):
        i = 1; j = num
        while i <= 15:
            while i < 15 and ladder[i][j] == 0:
                i += 1
            if ladder[i][j] == 1:
                j += 1
            elif ladder[i][j] == -1:
                j -= 1
            i += 1
        result.append(j)
    return result

result = simulate(make_ladder(init_info))
if result == [i+1 for i in range(n)]:
    print(0)
    exit(0)

selected = []
mn = m
def choose(i):
    global mn
    if i == m:
        if result == simulate(make_ladder(selected)):
            mn = min(mn, len(selected))
        return
    selected.append(init_info[i])
    choose(i+1)
    selected.pop()
    choose(i+1)
                
choose(0)
print(mn)