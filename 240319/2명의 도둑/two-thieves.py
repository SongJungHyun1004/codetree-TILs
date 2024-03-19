n, m, c = map(int, input().split())
room = [
    list(map(int, input().split()))
    for _ in range(n)
]
selected = []
def choose(i, stuffs):
    global value
    if i == m:
        new_value = 0
        weight = 0
        for j in selected:
            weight += stuffs[j]
            if weight > c:
                return
            new_value += stuffs[j]**2
        value = max(value, new_value)
        return
    selected.append(i)
    choose(i+1, stuffs)
    selected.pop()
    choose(i+1, stuffs)

mx = 0
for i in range(n):
    for j in range(n-m+1):
        stuffs1 = room[i][j:j+m]
        for k in range(i, n):
            if i == k:
                for l in range(j+m, n-m+1):
                    stuffs2 = room[k][l:l+m]
                    value = 0
                    choose(0, stuffs1)
                    tmp = value
                    value = 0
                    choose(0, stuffs2)
                    mx = max(mx, tmp+value)
            else:
                for l in range(n-m+1):
                    stuffs2 = room[k][l:l+m]
                    value = 0
                    choose(0, stuffs1)
                    tmp = value
                    value = 0
                    choose(0, stuffs2)
                    mx = max(mx, tmp+value)
        
print(mx)