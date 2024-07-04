# 변수 선언 및 입력:
a = input()
b = input()
delete = list(map(int, input().split()))

n = len(a)
m = len(b)
skip = [False for _ in range(n)]


def is_possible(mid):
    b_idx = 0
    # mid번째까지 문자열을 지웁니다.
    for i in range(mid):
        skip[delete[i] - 1] = True
    # 문자열을 지웠을 때, 이 문자열이 부분문자열이 되는지 확인합니다.
    for i in range(n):
        if skip[i]: 
            continue
        if b_idx < m and a[i] == b[b_idx]:
            b_idx += 1
    
    return b_idx == m


lo = 0                      # 답이 될 수 있는 가장 작은 숫자 값을 설정합니다.
hi = n                      # 답이 될 수 있는 가장 큰 숫자 값을 설정합니다.
ans = -1                    # 답을 저장합니다.

while lo <= hi:             # [lo, hi]가 유효한 구간이면 계속 수행합니다.
    mid = (lo + hi) // 2    # 가운데 위치를 선택합니다.
    if is_possible(mid):    # 결정문제에 대한 답이 Yes라면
        lo = mid + 1        # 오른쪽에 조건을 만족하는 숫자가 더 있을 가능성 때문에 left를 바꿔줍니다.
        ans = max(ans, mid) # 답의 후보들 중 최댓값을 계속 갱신해줍니다.
    else:
        hi = mid - 1        # 결정문제에 대한 답이 No라면 right를 바꿔줍니다.

    # mid번째까지 문자열을 되돌려 놓습니다.
    for i in range(mid):
        skip[delete[i] - 1] = False

# 정답을 출력합니다.
print(ans + 1)