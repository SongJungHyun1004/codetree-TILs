# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
edges = []

uf = [0] * (n * m + 1)

# n개의 줄에 대해 가로 간선을 모두 입력받습니다.
for i in range(1, n + 1):
    costs = list(map(int, input().split()))
    for j in range(1, m):
        # 각 칸을 1부터 n * m까지 번호를 매겨줍니다.
        x = (i - 1) * m + j
        y = (i - 1) * m + j + 1

        edges.append((costs[j - 1], x, y))

# n - 1개의 줄에 대해 세로 간선을 모두 입력받습니다.
for i in range(1, n):
    costs = list(map(int, input().split()))
    for j in range(1, m + 1):
        # 각 칸을 1부터 n * m까지 번호를 매겨줍니다.
        x = (i - 1) * m + j
        y = i * m + j

        edges.append((costs[j - 1], x, y))


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y


# cost 순으로 오름차순 정렬을 진행합니다.
edges.sort()

# uf 값을 초기값을 적어줍니다.
for i in range(1, n * m + 1):
    uf[i] = i

# cost가 낮은 간선부터 순서대로 보며
# 아직 두 노드가 연결이 되어있지 않을 경우에만
# 해당 간선을 선택하고 두 노드를 합쳐주면서
# mst를 만들어줍니다.
ans = 0
for cost, x, y in edges:
    # x, y가 연결되어 있지 않다면
    if find(x) != find(y):
        # 해당 간선은 MST에 속하는 간선이므로
        # 답을 갱신해주고
        # 두 노드를 연결해줍니다.
        ans += cost
        union(x, y)

print(ans)