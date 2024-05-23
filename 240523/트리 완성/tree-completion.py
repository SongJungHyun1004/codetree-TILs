import sys
input = sys.stdin.readline

n, m = map(int, input().split())
uf = [i for i in range(n+1)]

def find(x):
    if x == uf[x]:
        return x
    return find(uf[x])

def union(a, b):
    x = find(a)
    y = find(b)
    if x > y:
        uf[x] = y
    else:
        uf[y] = x

# 최대로 사용할 간선
mx_cnt = 0
for _ in range(m):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)
        mx_cnt += 1

# 제거되어야 할 간선 m - mx_cnt
# 추가되어야 할 간선 n-1 - mx_cnt

print(m - mx_cnt + n-1 - mx_cnt)