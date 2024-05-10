import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(x, depth):
    if len(tree[x]) == 1 and x != 1:  # 리프 노드인 경우
        return depth % 2  # 리프 노드에서 루트 노드까지의 깊이가 홀수인지 짝수인지 반환
    total = 0
    visited[x] = True
    for nx in tree[x]:
        if not visited[nx]:
            total += dfs(nx, depth + 1)
    return total

visited = [False] * (n+1)
# 루트 노드에서 시작하여 게임의 결과를 계산
result = dfs(1, 0)
# 결과가 홀수이면 a의 승리, 짝수이면 b의 승리
print(1 if result % 2 else 0)