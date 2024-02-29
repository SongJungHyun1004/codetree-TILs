from collections import deque
n = int(input())
MAX = 2*n+1 #연산과정 중 나올 수 있는 최대 숫자
mn = n-1 #최대 연산 횟수로 초기화
visited = [False]*(MAX+1)
op = [0]*(MAX+1)
def bfs(num):
    q = deque([num])
    while q:
        cur = q.popleft()
        if cur == 1:
            return
        nxt = cur+1
        if nxt <= MAX and not visited[nxt]:
            q.append(nxt)
            visited[nxt] = True
            op[nxt] = op[cur]+1
        nxt = cur-1
        if nxt > 1 and not visited[nxt]:
            q.append(nxt)
            visited[nxt] = True
            op[nxt] = op[cur]+1
        if cur % 2 == 0:
            nxt = cur//2
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                op[nxt] = op[cur]+1
        if cur % 3 == 0:
            nxt = cur//3
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
                op[nxt] = op[cur]+1
bfs(n)
print(op[1])