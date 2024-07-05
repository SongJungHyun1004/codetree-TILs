# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
edges = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

uf = [0] * (n + 1)


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


# cost 순으로 오름차순 정렬을 진행합니다.
edges.sort(key=lambda x: x[2])

# uf 값을 초기값을 적어줍니다.
for i in range(1, n + 1):
    uf[i] = i

# cost가 낮은 간선부터 순서대로 보며
# 아직 두 노드가 연결이 되어있지 않을 경우에만
# 해당 간선을 선택하고 두 노드를 합쳐주면서
# mst를 만들어줍니다.
ans = 0
last_cost = 0 # 마지막 간선의 가중치를 저장합니다.
for x, y, cost in edges:
    # x, y가 연결되어 있지 않다면
    if find(x) != find(y):
        # 해당 간선은 MST에 속하는 간선이므로
        # 답을 갱신해주고
        # 두 노드를 연결해줍니다.
        ans += cost
        last_cost = cost
        union(x, y)

# MST에서 가중치가 가장 큰 마지막 간선을 제외한 것이 답이 됩니다.
print(ans - last_cost)