# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

edges = []

uf = [0] * (n + 1)


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X, Y = find(x), find(y)
    uf[X] = Y


def mst():
    # uf 값을 초기값을 적어줍니다.
    for i in range(1, n + 1):
        uf[i] = i
    
    # cost가 낮은 간선부터 순서대로 보며
    # 아직 두 노드가 연결이 되어있지 않을 경우에만
    # 해당 간선을 선택하고 두 노드를 합쳐주면서
    # mst를 만들어줍니다.
    total_cost = 0
    for cost, x, y in edges:
        # x, y가 연결되어 있지 않다면
        if find(x) != find(y):
            # 해당 간선은 MST에 속하는 간선이므로
            # 답을 갱신해주고
            # 두 노드를 연결해줍니다.
            total_cost += cost
            union(x, y)

    return total_cost


# m개의 간선의 정보를 전부 입력받습니다.
for _ in range(m):
    x, y, cost = tuple(map(int, input().split()))
    edges.append((1 - cost, x, y))

# cost 순으로 오름차순 정렬을 진행합니다.
edges.sort()

# 최소 MST를 구합니다.
ans_min = mst()

# cost 순으로 내림차순 정렬을 진행합니다.
edges.sort(reverse=True)

# 최대 MST를 구합니다.
ans_max = mst()

# 정답은 최대 비용으로 만든 mst에서 최소 비용으로 만든 mst의 비용을 빼면 됩니다.
print(ans_max * ans_max - ans_min * ans_min)