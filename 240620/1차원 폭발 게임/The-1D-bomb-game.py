n, m = map(int, input().split())
bombs = []
for _ in range(n):
    bombs.append(int(input()))
bombs = bombs[::-1]

def simulate():
    while True:
        isExploded = False
        i = 0
        while i < len(bombs):
            j = i+1
            cnt = 1
            while j < len(bombs) and bombs[i] == bombs[j]:
                cnt += 1
                j += 1 
            if cnt >= m:
                isExploded = True
                for _ in range(cnt):
                    bombs.pop(i)
            else:
                i += 1

        if not isExploded:
            break



simulate()
print(len(bombs))
bombs = bombs[::-1]
for bomb in bombs:
    print(bomb)