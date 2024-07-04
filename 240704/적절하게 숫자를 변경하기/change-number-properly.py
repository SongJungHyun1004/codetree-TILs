import sys

MAX_K = 4
INT_MIN = -sys.maxsize    

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
a = [
    0
    for _ in range(n + 1)
]

# dp[i][j][k] :
# i번째 숫자까지 고려했고
# 그 동안 숫자를 j번 변경했고
# 마지막으로 사용한 숫자가 k라 했을 때 (k는 1, 2, 3, 4중에 하나)
# 얻을 수 있는 최대 유사도
dp = [
    [
        [0 for i in range(MAX_K + 1)]
        for _ in range(m + 1)
    ]
    for _ in range(n + 1)
]


def initialize():
    # 최댓값을 구하는 문제이므로, 
    # 초기에는 전부 INT_MIN을 넣어줍니다.
    for i in range(1, n + 1):
        for j in range(0, m + 1):
            for k in range(1, MAX_K + 1):
                dp[i][j][k] = INT_MIN
    
    # 첫 번째 숫자가 k인 경우를 전부 초기 조건으로 설정해줍니다.
    # 첫 번재 숫자가 k인 경우
    # 첫 번째 숫자까지 그 동안 숫자를 0번 변경했고 마지막으로 적은 숫자가 k이며,
    # 얻을 수 있는 유사도는 a[1]=k인 경우에는 1, 아닌 경우에는 0이 되어야 하므로
    # dp[1][0][k] 에 알맞는 값을 설정해줍니다.
    for k in range(1, MAX_K + 1):
        dp[1][0][k] = 1 if a[1] == k else 0


given_seq = list(map(int, input().split()))
a[1:] = given_seq[:]

initialize()

for i in range(2, n + 1):
    # i번째 숫자까지 고려해봤을 때
    # 그 동안 숫자를 j번 변경했고
    # 마지막으로 사용한 숫자가 k라 했을 때 (k는 1, 2, 3, 4중에 하나)
    # 얻을 수 있는 최대 유사도를 계산합니다.

    # 이러한 상황을 만들기 위한 선택지는 크게 2가지 입니다.
    for j in range(0, m + 1):
        for k in range(1, MAX_K + 1):
            # i - 1번째에 사용한 숫자 l을 정합니다.
            for l in range(1, MAX_K + 1):
                # Case 1
                # i번째 숫자에 k를 사용했지만, 숫자 변경이 일어나지 않은 경우입니다.
                # 따라서 숫자 변경이 없기 위해서는 l = k인 경우에만 유효한 경우이며, 
                # 숫자 변경 없이 지금까지의 총 변경 횟수가 j가 되려면
                # i - 1번째 까지의 총 변경 횟수 역시 j여야 하므로
                # dp[i - 1][j][l]에 
                # i번째 숫자에 k를 사용하므로 새롭게 얻어지는 유사도를 더한 값을
                # 얻을 수 있습니다.

                if l == k:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][l] + (a[i] == k))

                # Case2
                # i번째 숫자에 k를 사용하여 숫자 변경이 일어난 경우입니다.
                # 따라서 숫자 변경이 일어나기 위해서는 l != k인 경우에만 유효하며, 
                # 숫자 변경이 발생해 지금까지의 총 변경 횟수가 j가 되려면
                # i - 1번째 까지의 총 변경 횟수는 j-1이어야 하므로
                # dp[i - 1][j - 1][l]에 
                # i번째 숫자에 k를 사용하므로 새롭게 얻어지는 유사도를 더한 값을
                # 얻을 수 있습니다.
                # 당연히 j > 0인 경우에만 만들어질 수 있는 경우입니다.
                if l != k and j > 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][l] + (a[i] == k))

# n개의 숫자에 대해 전부 고려했을 때,
# 숫자를 변경한 횟수가 m을 넘지 않으면서 
# 마지막으로 사용한 숫자가 k인 경우 중
# 가장 높은 유사도를 얻을 수 있는 경우를 선택합니다.

ans = max([
    dp[n][j][k]
    for j in range(m + 1)
    for k in range(1, MAX_K + 1)
])

print(ans)