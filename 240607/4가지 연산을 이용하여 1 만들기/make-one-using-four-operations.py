from collections import deque
MAX = 10**6
n = int(input())
visited = [False]*(MAX+1)

def in_range(x):
    return 1<=x<=MAX

def bfs():
    q = deque([(n, 0)])
    visited[n] = True
    while q:
        x, cnt = q.popleft()
        if x == 1:
            return cnt
        nx = x - 1
        if in_range(nx) and not visited[nx]:
            visited[nx] = True
            q.append((nx, cnt+1))
        nx = x + 1
        if in_range(nx) and not visited[nx]:
            visited[nx] = True
            q.append((nx, cnt+1))
        if x%2 == 0:
            nx = x//2
            if in_range(nx) and not visited[nx]:
                visited[nx] = True
                q.append((nx, cnt+1))
        if x%3 == 0:
            nx = x//3
            if in_range(nx) and not visited[nx]:
                visited[nx] = True
                q.append((nx, cnt+1))

print(bfs())