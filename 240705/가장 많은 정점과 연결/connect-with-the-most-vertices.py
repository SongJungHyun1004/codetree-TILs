# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))

uf = [0] * (n + 1)

visited = [0] * (n + 1)

cost_list = []

# min_cost의 초기값이 주어집니다.
min_cost = [0] + list(map(int, input().split()))

# uf 값을 초기값을 적어줍니다.
for i in range(1, n + 1):
    uf[i] = i


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y

    # 각 그룹의 최소비용을 관리합니다.
    min_cost[Y] = min(min_cost[Y], min_cost[X])


for _ in range(m):
    x, y = tuple(map(int, input().split()))

    # 이미 연결되어 있으므로 union을 진행합니다.
    union(x, y)

# 각 그룹들에 대해 min_cost값을 모아줍니다.
for i in range(1, n + 1):
    I = find(i)

    # 중복되는 그룹은 패스합니다.
    if visited[I]:
        continue
    
    visited[I] = True
    cost_list.append(min_cost[I])

# min_cost를 오름차순으로 정렬합니다.
cost_list.sort()

# 가장 작은 min_cost 쪽과 간선을 연결하는 것이 최선입니다.
ans = 0
for i in range(1, len(cost_list)):
    ans += cost_list[0] + cost_list[i]

if ans <= k:
    print(ans)
else:
    print("NO")