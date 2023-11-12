N, H, T = map(int, input().split())
ground = list(map(int, input().split()))
mn = float('inf')
for i in range(N-T+1):
    cost = 0
    for j in range(i, i+T):
        cost += abs(H-ground[j])
    mn = min(mn, cost)
print(mn)