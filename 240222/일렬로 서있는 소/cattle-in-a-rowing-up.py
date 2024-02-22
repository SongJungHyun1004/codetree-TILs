def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next

n = int(input())
pos = sorted([int(input()) for _ in range(n)])

cnt = 0
for cows in combinations(pos, 3):
    x, y, z = cows
    if x < y < z and y-x <= z-y <= 2*(y-x):
        cnt += 1

print(cnt)