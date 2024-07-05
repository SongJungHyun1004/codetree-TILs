import heapq

# 변수 선언 및 입력:
n = int(input())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
ans = [0] * (n + 1)

# 인접리스트로 관리합니다.
chars = [' '] + list(input().split())
for i in range(1, n):
    c = chars[i]
    if c == '<':
        edges[i].append(i + 1) 
    else:
        edges[i + 1].append(i)


def topological_sort(reverse):
    pq = []

    # indegree를 주어진 그래프를 이용하여 다시 계산합니다.
    for i in range(1, n + 1):
        indegree[i] = 0

    for i in range(1, n + 1):
        for x in edges[i]:
            indegree[x] += 1
    
    # 처음 indegree 값이 0인 곳이 루트가 됩니다.
    # 이 노드들을 queue에 넣어주고, 정답으로 미리 저장해 놓습니다.
    for i in range(1, n + 1):
        if not indegree[i]:
            # reverse값에 따라 최대 최소가 나오도록 조정합니다.
            heapq.heappush(pq, i if not reverse else -i)
    
    # 위상정렬을 진행합니다.
    # 항상 더 우선순위가 높은 값을 뽑기 위해 priority queue로 관리합니다.
    # priority queue에 원소가 남아있다면 계속 진행합니다.
    cnt = 1
    while pq:
        # 가장 앞에 있는 원소를 뽑아줍니다.
        # reverse값에 따라 최대 최소가 나오도록 조정합니다.
        x = heapq.heappop(pq) if not reverse else -heapq.heappop(pq)

        ans[x] = cnt
        cnt += 1

        # x에서 갈 수 있는 모든 곳을 탐색합니다.
        for y in edges[x]:
            # 해당 노드의 indegree를 1만큼 감소시켜줍니다.
            indegree[y] -= 1

            # indegree가 0이 되었다면
            # queue에 새로 넣어줍니다.
            if not indegree[y]:
                # reverse값에 따라 최대 최소가 나오도록 조정합니다.
                heapq.heappush(pq, y if not reverse else -y)

    # 답을 출력합니다.
    for i in range(1, n + 1):
        print(f"{ans[i]:03d}", end="")
    print()


# 사전순으로 앞선 답이 나오도록 합니다.
topological_sort(False)
# 사전순으로 가장 뒤에 있는 답이 나오도록 합니다.
topological_sort(True)