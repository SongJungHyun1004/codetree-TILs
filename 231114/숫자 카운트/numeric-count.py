n = int(input())
lst = []
for _ in range(n):
    query, s, b = input().split()
    s, b = int(s), int(b)
    lst.append([list(map(int, query)), s, b])

def isPossible(num):
    for l in lst:
        c1, c2 = 0, 0
        query, s, b = l[0], l[1], l[2]
        for i in range(3):
            if num[i] == query[i]:
                c1 += 1
            elif num[i] in query:
                c2 += 1
        if c1 != s or c2 != b:
            return False
    return True

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            if isPossible([i, j, k]):
                cnt += 1
print(cnt)