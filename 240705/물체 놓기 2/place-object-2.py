n, kk = map(int, input().split())
cost = [0] + [
    int(input()) for _ in range(n)
]

board = [[0 for _ in range(n + 1)]] + [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]

# dp[i] : 
# 1번을 시작으로 각 정점마다 방문한 여부를
# x1, x2, ..., xk라 헀을 때 
# 2^x1 + 2^x2 + ... + 2^xk 값이 i이고 (bitmask된 정수값이 i)
# 가능한 최소 비용
# 최소를 구하는 문제이므로 초기값으로 매우 큰 값을 넣어줍니다.
dp = [10**9 for _ in range(1 << n)]

# 초기조건은
# 아무것도 안 고른 상태입니다.
# 이 때에는 0을 넣어줍니다.
dp[0] = 0

# 뿌려주는 방식의 dp를 진행합니다.
# dp[i]가 계산이 되어있다는 가정하에서
# 그 다음 상태값을 갱신합니다.
for i in range(1 << n):
    # 그 다음 물체를 k번 정점에 놓게 되는 경우
    # 상태값을 계산하여 최솟값을 갱신해줍니다.
    for k in range(1, n + 1):
        # k번 지점에 이미 물체가 있다면
        # 중복 방문은 조건상 불가하므로 패스합니다.
        # dp의 편의를 위해 board 배열을 1번 인덱스부터 입력받았으므로
        # bitmasking 할 때에는 0번 인덱스 기준으로 관리해줍니다. (1을 빼줍니다)
        if ((i >> (k - 1)) & 1) == 1:
            continue
        
        # k번 지점으로 물체를 놓기 위해 필요한 최소 비용을 찾습니다.
        val = dp[i]
        mn_cost = cost[k]
        for l in range(1, n + 1):
            if ((i >> (l - 1)) & 1) == 1:
                mn_cost = min(mn_cost, board[l][k])
        
        # k번 지점으로 물체를 놓았을 때의 정보를 갱신해줍니다.
        dp[i + (1 << (k - 1))] = min(
            dp[i + (1 << (k - 1))], dp[i] + mn_cost
        )

# 가능한 최솟값을 출력합니다.
ans = 10**9
for i in range(1 << n):
    object_num = 0

    for k in range(1, n + 1):
        if ((i >> (k - 1)) & 1) == 1:
            object_num += 1
        
    if object_num >= kk:
        ans = min(ans, dp[i])

print(ans)