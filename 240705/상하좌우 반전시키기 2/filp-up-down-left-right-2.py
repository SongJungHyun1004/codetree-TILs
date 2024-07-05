n, m = map(int, input().split())

board = [[0 for _ in range(m + 1)]] + [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, -1, 0, 1, 0]
dys = [0, 0, -1, 0, 1]

# 변수 선언
board_original = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]

def isOutrange(x, y):
    return not (1 <= x and x <= n and 1 <= y and y <= m)

ans = 10**9

   
for i in range(1, n + 1):
    for j in range(1, m + 1):
        board_original[i][j] = board[i][j]

# 1번째 행을 2^m가지의 방법으로 모든 방법을 눌러봅니다.
# 그 다음부터는 2번째 행은 1번 행을 전부 1로 만들기 위해 방법이 제한됩니다.
# 이를 바탕으로 최소 횟수를 구해 보겠습니다.
for state in range(1 << m):
    # board를 초기화합니다.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            board[i][j] = board_original[i][j]

    # 우선 2^m가지의 방법으로 모두 눌러보고 그에 맞게 board를 바꿔줍니다.
    for y in range(1, m + 1):
        if (state >> (y - 1)) & 1:
            x = 1
            for (dx, dy) in zip(dxs, dys):
                nx = x + dx
                ny = y + dy

                if isOutrange(nx, ny): continue

                board[nx][ny] = 1 - board[nx][ny]

    # 해당 방법으로 눌렀을 때
    # 숫자를 눌러야 할 횟수를 num에 기록합니다.
    num = 0
    for y in range(1, m + 1):
        if (state >> (y - 1)) & 1:
            num += 1

    # 2번 행부터 차근차근 버튼을 눌러봅니다.
    cnt = 0
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            # board[i - 1][j]가 0이면 누릅니다.
            if board[i - 1][j] == 0:
                num += 1
                for (dx, dy) in zip(dxs, dys):
                    nx = i + dx
                    ny = j + dy

                    if isOutrange(nx, ny):
                        continue
                    
                    board[nx][ny] = 1 - board[nx][ny]
    
    # 다 채워졌는지 확인합니다.
    full_filled = True
    for j in range(1, m + 1):
        if not board[n][j]: full_filled = False
    
    if full_filled:
        ans = min(ans, num)

# 숫자를 모두 1로 만들기 위해 눌러야 할 최소 횟수를 출력합니다.
# 만약 만드는 것이 불가능하다면 -1을 출력합니다.
if ans == 10**9:
    print(-1)
else:
    print(ans)