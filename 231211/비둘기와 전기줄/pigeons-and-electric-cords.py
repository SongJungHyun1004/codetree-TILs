n = int(input())
pigeons = [-1]*11
cnt = 0
for _ in range(n):
    num, pos = map(int, input().split())
    if pigeons[num] == -1:
        pigeons[num] = pos
    elif pigeons[num] != pos:
        pigeons[num] = 1-pigeons[num]
        cnt += 1
print(cnt)