# 변수 선언 및 입력: 
n = int(input())
arr = list(map(int, input().split()))
L, R = [0] * n, [0] * n

# 총 합을 계산합니다.
total_sum = sum(arr)

# 총 합이 4로 나누어 떨어지지 않으면 답은 0입니다.
if total_sum % 4 != 0:
    print(0)
    quit()

# 각 구간 내 합이 되어야 할 target_sum
# 값을 설정합니다.
target_sum = total_sum // 4

# L 배열을 채워줍니다.
# L[i] = 0번부터 i번까지 합이 target_sum인 구간을 
#        정확히 2개 만들 수 있는 서로 다른 가지수
L[0] = 0
sum_val = arr[0] # 지금까지의 합
cnt = 1 if sum_val == target_sum else 0 # 합이 정확히 target_sum이 되었던 횟수
for i in range(1, n):
    sum_val += arr[i]
    # 합이 2 * target_sum이 되면
    # 정확히 2개의 구간을 만들 수 있는 가능성이 있으므로
    # cnt값을 기록해줍니다.
    if sum_val == 2 * target_sum:
        L[i] = cnt
    
    # 합이 target_sum인 경우
    # cnt 값을 갱신해줍니다.
    if sum_val == target_sum:
        cnt += 1

# R 배열을 채워줍니다.
# R[i] = i번부터 n - 1번까지 합이 target_sum인 구간을 
#        정확히 2개 만들 수 있는 서로 다른 가지수
R[n - 1] = 0
sum_val = arr[n - 1] # 지금까지의 합
cnt = 1 if sum_val == target_sum else 0  # 합이 정확히 target_sum이 되었던 횟수
for i in range(n - 2, -1, -1):
    sum_val += arr[i]
    # 합이 2 * target_sum이 되면
    # 정확히 2개의 구간을 만들 수 있는 가능성이 있으므로
    # cnt값을 기록해줍니다.
    if sum_val == 2 * target_sum:
        R[i] = cnt
    
    # 합이 target_sum인 경우
    # cnt 값을 갱신해줍니다.
    if sum_val == target_sum:
        cnt += 1

# 각 위치 i에 대해
# [0, i] 까지는 합이 target_sum인 구간을 정확히 2개를 만들고
# [i + 1, n] 까지도 합이 target_sum인 구간을 정확히 2개를 만든다고 했을 때 
# 가능한 가지수를 세줍니다.
ans = 0
for i in range(1, n - 1):
    ans += L[i] * R[i + 1]
print(ans)