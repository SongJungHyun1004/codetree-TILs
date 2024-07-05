# 변수 선언 및 입력:
n = int(input())

# n개의 점의 정보를 전부 입력받습니다.
points = []
for i in range(1, n + 1):
    x, y, z = tuple(map(int, input().split()))
    points.append((x, y, z, i))

edges = []

uf = [0] * (n + 1)

def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y


def push(p1, p2):
    x1, y1, z1, idx1 = p1
    x2, y2, z2, idx2 = p2
    cost = min(min(abs(x1 - x2), abs(y1 - y2)), abs(z1 - z2))
    edges.append((cost, idx1, idx2))


# 모든 점을 x 순으로 정렬합니다.
points.sort(key=lambda x : x[0])
# 각 정렬된 점에서 연속한 순서대로 간선을 이어줍니다.
for i in range(n - 1):
    push(points[i], points[i + 1])

# 모든 점을 y 순으로 정렬합니다.
points.sort(key=lambda x : x[1])
# 각 정렬된 점에서 연속한 순서대로 간선을 이어줍니다.
for i in range(n - 1):
    push(points[i], points[i + 1])

# 모든 점을 z 순으로 정렬합니다.
points.sort(key=lambda x : x[2])
# 각 정렬된 점에서 연속한 순서대로 간선을 이어줍니다.
for i in range(n - 1):
    push(points[i], points[i + 1])

# cost 순으로 오름차순 정렬을 진행합니다.
edges.sort()

# uf 값을 초기값을 적어줍니다.
for i in range(1, n + 1):
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