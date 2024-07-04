# 변수 선언 및 입력
n, k, l = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


# h 이상의 수를 h개 이상
# 만들 수 있을지 판단합니다.
def is_possible(h):
    # 이미 크기가 큰 h개의 수들에 대해
    # 전부 h 이상이 되기 위해
    # 새로 적혀야 하는 번호의 수를 계산합니다.
    cnt = 0
    for i in range(n - h, n):
        if arr[i] < h:
            cnt += h - arr[i]

    # 새로 적혀야 하는 번호의 수가 최대로 적을 수 있는 수인 k * l 이하이며
    # arr[n - h] + k가 h 이상이어야만 k개의 포스트잇으로 해결이 가능합니다.
    return cnt <= k * l and arr[n - h] + k >= h

   
# 주어진 수들을
# 오름차순으로 정렬합니다.
arr.sort()

left = 1                              # 답이 될 수 있는 가장 작은 값을 설정합니다.
right = n                             # 답이 될 수 있는 가장 큰 값을 설정합니다.
ans = 0                               # 답을 저장합니다.

while left <= right:                  # [left, right]가 유효한 구간이면 계속 수행합니다.
    mid = (left + right) // 2         # 가운데 위치를 선택합니다.
    if is_possible(mid):              # 결정문제에 대한 답이 Yes라면
        left = mid + 1                # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 left를 바꿔줍니다.
        ans = max(ans, mid)           # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:
        right = mid - 1               # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

print(ans)