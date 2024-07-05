n, m = map(int, input().split())

board = [[0 for _ in range(m + 1)]] + [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]

# dp[i][j] : 
# 1번 행을 시작으로 i번 행까지 칸을 채웠을 때
# 각 i번 행에서 각 열마다 칸을 선택했는지 여부를
# x1, x2, ..., xk라 헀을 때 
# 2^x1 + 2^x2 + ... + 2^xk 값이 j라 하면 (bitmask된 정수값이 j)
# 해당 상태에서 최대로 선택할 수 있는 빈 칸의 수

# 초기값으로 -1을 넣어 해당 상태가 불가능함을 표기해줍니다.
dp = [
    [-1 for _ in range(1 << m)]
    for _ in range(n + 1)
]

# 초기조건은
# 0번째 행에서 아무것도 안 고른 상태입니다.
# 이 때에는 0을 넣어줍니다.
dp[0][0] = 0

# 뿌려주는 방식의 dp를 진행합니다.
# dp[i][j]가 계산이 되어있다는 가정하에서
# 그 다음 상태값을 갱신합니다.
for i in range(n):
    for j in range(1 << m):
        # dp값이 -1이라면
        # 해당 값은 불가능한 상황이므로 패스합니다.
        if dp[i][j] == -1:
            continue
        
        for k in range(1 << m):
            # 그다음 줄의 state에 대해 해당 값을 만들 수 있는지 판단하고 답을 갱신해줍니다.
            
            # 두 값의 비트가 겹친다면
            # 상하로 인접한 칸이 있음을 의미하므로 패스합니다.
            if k & j: continue

            # k에서 연속된 두 비트의 값이 1이라면
            # 좌우로 인접한 칸이 있음을 의미하므로 패스합니다.
            is_overlap = False
            for x in range(m - 1):
                if ((k >> x) & 1) and ((k >> (x + 1)) & 1):
                    is_overlap = True
            if is_overlap: continue

            # k에서 선택한 칸 중에 벽이 있으면
            # 불가능한 상황이므로 패스합니다.
            is_imp = False
            for x in range(m):
                if ((k >> x) & 1) and board[i + 1][x + 1] == 1:
                    is_imp = True
            if is_imp: continue

            # i + 1번째 줄에 추가로 선택되는 칸의 개수 num을 계산해 준 뒤,
            # dp값을 갱신해줍니다.
            num = 0
            for x in range(m):
                if (k >> x) & 1: num += 1

            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + num)

# 선택할 수 있는 칸의 개수의 최댓값을 출력합니다.
ans = 0
for i in range(1 << m):
    ans = max(ans, dp[n][i])
print(ans)