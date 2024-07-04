# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))
L = [0] * n
R = [0] * n

ans = 0

# L 배열을 채워줍니다.
# L[i] = 0번부터 i번 원소 중 최댓값
L[0] = arr[0]
for i in range(1, n):
    L[i] = max(L[i - 1], arr[i])

# R 배열을 채워줍니다.
# R[i] = i번부터 n - 1번 원소 중 최댓값
R[n - 1] = arr[n - 1]
for i in range(n - 2, -1, -1):
    R[i] = max(R[i + 1], arr[i])

# i번째 숫자가 세 숫자 중 가운데 숫자라고 했을 때
# 가능한 최대 합 중 최댓값을 갱신해줍니다.
for i in range(2, n - 2):
    ans = max(ans, L[i - 2] + arr[i] + R[i + 2])

print(ans)