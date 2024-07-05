import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]

arr = [0] * (n + 1)
dp = [0] * (n + 1) # dp[i] : i번째 노드에 최종적으로 적히게 되는 값

# n - 1개의 간선 정보를 입력받습니다.
for i in range(2, n + 1):
    t, a, p = tuple(map(int, input().split()))
    # 간선 정보를 인접리스트에 넣어줍니다.
    # 부모가 이미 주어진 상황이므로 
    # p . i 에 해당하는 간선만 만들어도 충분합니다.
    edges[p].append(i)

    # 각 노드에 해당하는 값을 기록합니다.
    arr[i] = a if t == 1 else -a


# DFS를 통해 연결된 모든 정점을 순회합니다.
# 동시에 dp값을 계산해줍니다.
def dfs(x):
    # 노드 x에 연결된 간선을 살펴보며 전부 방문해줍니다.
    for y in edges[x]:
        dfs(y)

    # 이제 퇴각하기 전에
    # 각각의 자식들을 다시 순회하며 
    # dp[x] 값을 갱신해줍니다.
    dp[x] = arr[x] # 초기 값을 설정해줍니다.
    for y in edges[x]:
        # 자식에 적힌 값이 양수인 경우에만 그 값을 더해줍니다.
        if dp[y] > 0:
            dp[x] += dp[y]

    
# 1번 정점을 시작으로 DFS를 진행하며 값을 갱신합니다.
dfs(1)

# 1번 노드에 적혀있는 값을 출력합니다.
print(dp[1])