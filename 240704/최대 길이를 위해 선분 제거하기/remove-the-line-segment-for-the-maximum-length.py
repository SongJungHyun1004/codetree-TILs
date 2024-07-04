import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

weights = [0] * n # 각 선분을 제외했을 때 빠지게 되는 길이를 저장합니다.

# 각 선분을 두 지점으로 나눠 담은 뒤,
# 정렬해줍니다.
# 이때 (x좌표, +1-1값, 선분 번호)
# 형태로 넣어줍니다.
# +1은 시작점
# -1은 끝점을 뜻합니다.
points = []
for i in range(n):
    x1, x2 = segments[i]
    points.append((x1, +1, i)) # 시작점
    points.append((x2, -1, i)) # 끝점

# 정렬을 진행합니다.
points.sort()

# 각 점을 순서대로 순회합니다.
# 각 선분을 제외했을 때 빠지게 되는 길이를
# 각 weights[index]에 표시해줍니다.
tot_length = 0       # 전체 길이의 합을 계산합니다.
segs = set()  # 현재 걸쳐져 있는 선분 번호를 관리합니다.
prev_x = -1          # 바로 직전 x값을 관리합니다.
for x, v, index in points:
    # 걸쳐져 있는 선분의 수는 segs의 크기와 같습니다.
    seg_cnt = len(segs)

    # 걸쳐져 있는 선분의 수가 1개 이상이라면
    # 전체 길이의 합을 갱신합니다.
    if seg_cnt > 0:
        tot_length += x - prev_x
    
    # 걸쳐져 있는 선분의 수가 정확히 1개라면
    # 해당 걸쳐져 있는 선분의 weights를 갱신합니다.
    if seg_cnt == 1:
        target_index = list(segs)[0]
        weights[target_index] += x - prev_x

    # 시작점인 경우입니다.
    if v == +1:
        # 걸쳐져 있는 선분 번호를 갱신합니다.
        segs.add(index)

    # 끝점인 경우입니다.
    else:
        # 걸쳐져 있는 선분 번호를 제거합니다.
        segs.remove(index)

    # 이전 x 값을 갱신해줍니다.
    prev_x = x

min_length = INT_MAX # 특정 선분을 제외했을 때 빠지게 되는 길이 중 최솟값을 계산합니다.
for i in range(n):
    min_length = min(min_length, weights[i])

print(tot_length - min_length)