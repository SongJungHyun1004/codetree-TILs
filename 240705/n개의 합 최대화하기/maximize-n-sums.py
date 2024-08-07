import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dp[i][j] : 
# i번째 행 직전까지 선택을 완료했고
# 지금까지 선택한 열의 위치가
# x1, x2, ..., xk가 되어
# 2^x1 + 2^x2 + ... + 2^xk 값이 j이 되었을 때 (bitmask된 정수값이 j)
# 가능한 최대 점수
dp = [
    [0] * (1 << n)
    for _ in range(n + 1)
]
  
# 초기값으로 아주 작은 값을 넣어줍니다.
for i in range(n + 1):
    for j in range(1 << n):
        dp[i][j] = INT_MIN

# 초기조건은
# 0번째 행 직전까지 선택을 완료했고
# 현재 state가 0인 상태입니다.
# 이 때에는 0을 넣어줍니다.
dp[0][0] = 0

# 뿌려주는 방식의 dp를 진행합니다.
# dp[i][j]가 계산이 되어있다는 가정하에서
# 그 다음 상태값을 갱신합니다.
for i in range(n):
    for j in range(1 << n):
        # j번 상태를 만들어내는게 정의상 불가능 하다면
        # 패스합니다.
        if dp[i][j] == INT_MIN:
            continue

        # i번째 행에는 k번 열을 고르게 되는 경우의
        # 상태값을 계산하여 최댓값을 갱신해줍니다.
        for k in range(n):
            # k번 열을 이미 선택한 적이 있다면
            # 중복 방문은 조건상 불가하므로 패스합니다.
            if ((j >> k) & 1) == 1:
                continue
            
            dp[i + 1][j + (1 << k)] = max(
                dp[i + 1][j + (1 << k)], dp[i][j] + board[i][k]
            )

# 가능한 최댓값을 출력합니다.
print(dp[n][(1 << n) - 1])