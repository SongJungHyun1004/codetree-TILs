from collections import deque

MAX_K = 100

# 변수 선언 및 입력:
n = int(input())
N = 0 # 새로 만들어진 그래프에서 노드의 수 입니다.

board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
renum = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [
    [False] * (n + 1)
    for _ in range(n + 1)
]
step = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

edges = []
uf = [0] * (MAX_K + 1)

# n행 n열의 격자 정보를 모두 입력받습니다.
for i in range(1, n + 1):
    row = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        board[i][j] = row[j]


def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and board[x][y] != -1


def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    uf[X] = Y


def bfs(sx, sy):
    q = deque()

    # visited 배열과
    # 최단거리 값을 저장할 step 배열 값을 초기화합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            visited[i][j] = False
            step[i][j] = -1

    # 시작 위치는 최단거리 값이 0이 됩니다.
    visited[sx][sy] = True
    step[sx][sy] = 0
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 이동이 불가능한 경우에는 패스합니다.
            if not can_go(nx, ny):
                continue

            visited[nx][ny] = True
            step[nx][ny] = step[x][y] + 1
            q.append((nx, ny))

            # bfs를 진행하며 탐사기지를 찾은 경우, 
            # 각 기지로부터의 거리를
            # 그래프의 형식으로 간선을 추가해줍니다.
            if board[nx][ny] == 1 or board[nx][ny] == 2:
                edges.append((step[nx][ny], renum[sx][sy], renum[nx][ny]))


def mst():
    # cost 순으로 오름차순 정렬을 진행합니다.
    edges.sort()

    # uf 값을 초기값을 적어줍니다
    for i in range(1, N + 1):
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

    # 모두 연결되어있는지를 판단하기 위해
    # is_all_connected라는 변수를 관리합니다.
    is_all_connected = True
    for i in range(2, N + 1):
        x = find(1)
        y = find(i)
        if x != y: 
            is_all_connected = False

    # 모두 연결되어 있다면 총 비용을 출력합니다.
    # 그렇지 않다면 불가능하다는 의미로 -1을 반환합니다.
    if is_all_connected:
        return total_cost
    else:
        return -1

   
# 기지마다 새로운 그래프에서의 정점 번호를 매겨줍니다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == 1 or board[i][j] == 2:
            N += 1
            renum[i][j] = N

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == 1 or board[i][j] == 2:
            # 탐사 기지가 있는 경우 해당 위치에서부터 bfs를 진행합니다.
            # bfs를 통해 각 기지까지의 최단거리를 구해줄 수 있습니다.
            bfs(i, j)

# MST를 계산합니다.
print(mst())