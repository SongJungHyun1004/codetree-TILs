n = int(input())
arr = list(map(int, input().split()))

MAX_K = 10

# dp[i][j][k] : [i, j] 구간에 있는 수들을 전부 하나로 합쳤을 때,
#               k를 남기면서 얻을 수 있는 최대 점수를 기록합니다.
dp = [
    [
        [0 for _ in range(MAX_K + 1)]
        for _ in range(n)
    ]
    for _ in range(n)
]

# pos[i][j][k] : [i, j] 구간에 있는 수들을 전부 하나로 합쳤을 때,
#                k를 남길 수 있는지 여부를 기록합니다.
pos = [
    [
        [False for _ in range(MAX_K + 1)]
        for _ in range(n)
    ]
    for _ in range(n)
]

   
# 구간의 크기가 1인 경우 dp값이 0, (그에 맞는 pos는 True)
# 구간의 크기가 2인 경우 dp값이 두 수의 합 (그에 맞는 pos는 True)가 되어야 합니다.
# dp[i][i + 1][abs(arr[i] - arr[i + 1])] = arr[i] + arr[i + 1]
# 이 초기조건이 됩니다.
for i in range(n):
    pos[i][i][arr[i]] = True
    if (i + 1) != n:
        dp[i][i + 1][abs(arr[i] - arr[i + 1])] = arr[i] + arr[i + 1]
        pos[i][i + 1][abs(arr[i] - arr[i + 1])] = True

# dp는 미리 구해져 있는 작은 문제를 가지고 큰 문제를 풀어야 하므로
# 이러한 유형의 경우 구간을 점점 넓혀가면서 dp값을 채워야만 합니다. 
# 따라서 구간의 크기를 3부터 n까지 증가하게 미리 정해줍니다.
for gap in range(3, n + 1):
    # 구간의 시작위치 i를 정해줍니다.
    for i in range(n - gap + 1):
        # 구간의 크기와 시작 위치가 정해져 있기에
        # 끝 위치는 자동으로 정해집니다.
        j = i + gap - 1

        # [i, j]가 되기 위해
        # 최종적으로 합쳐지는 두 수가
        # 각각 [i, k], [k + 1, j]로부터 온 결과들을 바탕으로
        # 가능한 답의 최댓값을 갱신해줍니다.
        for k in range(i, j):
            for x in range(MAX_K + 1):
                if not pos[i][k][x]: continue
                for y in range(MAX_K + 1):
                    if not pos[k + 1][j][y]: continue

                    score = dp[i][k][x] + dp[k + 1][j][y] + x + y
                    pos[i][j][abs(x - y)] = True
                    dp[i][j][abs(x - y)] = max(dp[i][j][abs(x - y)], score)

# 모든 수를 합치면서 얻는 최대 점수를 출력합니다.
ans = 0
for x in range(MAX_K + 1):
    ans = max(ans, dp[0][n - 1][x])

print(ans)