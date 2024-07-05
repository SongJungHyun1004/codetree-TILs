from collections import deque

# 변수 선언 및 입력:
n = int(input())

string_to_node = {}

edges = [[] for _ in range(n + 1)]
root = []
child = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 각 노드의 이름을 입력받습니다.
# 처음부터 노드의 이름 순으로 정렬해
# 노드의 번호를 매겨주면 구현이 쉽습니다.
nodes = [" "] + sorted(list(input().split()))
for i in range(1, n + 1):
    string_to_node[nodes[i]] = i

m = int(input())
# 인접리스트로 관리합니다.
for _ in range(m):
    x_str, y_str = tuple(input().split())

    x, y = string_to_node[x_str], string_to_node[y_str]

    edges[y].append(x) 
    indegree[x] += 1 # 진입차수를 갱신합니다.

# 처음 indegree 값이 0인 곳이 루트가 됩니다.
# 이 노드들을 queue에 넣어주고, 정답으로 미리 저장해 놓습니다.
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

        # indegree가 0인 지점들이 각 트리에서의 루트가 됩니다.
        root.append(i)

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # 해당 노드는 x노드의 바로 자식노드입니다.
        # queue에 새로 넣어주고, 자식노드 정보를 갱신합니다.
        if not indegree[y]:
            q.append(y)

            # 0이 되는 순간에 이용한 간선들이
            # 결국 트리에서의 실제 간선이 됩니다. 
            child[x].append(y)

# 자식 노드들을 이름 순으로 정렬합니다.
for i in range(1, n + 1):
    child[i].sort()

# 정답을 순서대로 출력합니다.
print(len(root))
for str_name in root:
    print(nodes[str_name], end=" ")
print()

for i in range(1, n + 1):
    print(nodes[i], end=" ")
    print(len(child[i]), end=" ")
    for str_name in child[i]:
        print(nodes[str_name], end=" ")
    print()