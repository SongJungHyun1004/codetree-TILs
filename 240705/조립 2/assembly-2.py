from collections import deque

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

edges = [[] for _ in range(n + 1)]

# 진입차수를 관리합니다.
indegree = [0] * (n + 1)
visited = [False] * (n + 1)

# 위상정렬을 위한 큐를 관리합니다.
q = deque()

# 만들 수 있는 조각들을 관리합니다.
ans = []

# 인접리스트로 관리합니다.
for _ in range(m):
    a, k = tuple(map(int, input().split()))
    nums = list(map(int, input().split()))
    for x in nums:
        # a번 조각을 만들기 위해서는 x번 조각이 필요합니다.
        # 간선의 방향을 주의합니다.
        edges[x].append(a) 
        indegree[a] += 1 # 진입차수를 갱신합니다.

# 현재 가지고 있는 조각들을 입력받습니다.
_ = int(input())
part_nums = list(map(int, input().split()))
for x in part_nums:
    q.append(x)
    visited[x] = True

# 위상정렬을 진행합니다.
# queue에 원소가 남아있다면 계속 진행합니다.
while q:
    # 가장 앞에 있는 원소를 뽑아줍니다.
    x = q.popleft()

    # 만들 수 있는 조각 목록에 x를 추가합니다.
    ans.append(x)

    # x에서 갈 수 있는 모든 곳을 탐색합니다.
    for y in edges[x]:
        # 이미 만들 수 있는 조각이면 넘어갑니다.
        if visited[y]: 
            continue

        # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
        indegree[y] -= 1

        # 비로소 indegree가 0이 되었다면
        # 해당 노드는 만들 수 있습니다.
        # queue에 새로 넣어주고, visited 배열을 갱신합니다.
        if not indegree[y]:
            q.append(y)
            visited[y] = True

# 정답을 오름차순으로 정렬합니다.
ans.sort()

# 정답을 순서대로 출력합니다.
print(len(ans))
for num in ans:
    print(num, end=" ")