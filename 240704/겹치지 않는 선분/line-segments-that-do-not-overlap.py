# 변수 선언 및 입력:
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

L, R = [0] * n, [0] * n

# x1 기준으로 정렬합니다.
segments.sort()

# L 배열을 채워줍니다.
# L[i] = 0번부터 i번까지 선분 중
#        최대 x2값
_, x2 = segments[0]
L[0] = x2
for i in range(1, n):
    _, x2 = segments[i]
    L[i] = max(L[i - 1], x2)

# R 배열을 채워줍니다.
# R[i] = i번부터 n - 1번까지 선분 중
#        최소 x2값
_, x2 = segments[n - 1]
R[n - 1] = x2
for i in range(n - 2, -1, -1):
    _, x2 = segments[i]
    R[i] = min(R[i + 1], x2)

# 각 선분 i에 대해
# 왼쪽에서 가장 멀리 뻗은 L[i - 1] 값과
# 오른쪽에서 가장 멀리 뻗은 R[i + 1] 값 모두와 겹치지 않는 경우에만
# 답을 갱신해줍니다.
ans = 0
for i in range(n):
    _, x2 = segments[i]
    # 왼쪽 선분과 겹치면 패스합니다.
    if i > 0 and L[i - 1] >= x2:
        continue
    # 오른쪽 선분과 겹치면 패스합니다.
    if i < n - 1 and R[i + 1] <= x2:
        continue
    
    # 답을 갱신합니다.
    ans += 1

print(ans)