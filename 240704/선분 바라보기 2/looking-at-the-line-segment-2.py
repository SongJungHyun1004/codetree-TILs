from sortedcontainers import SortedSet

# 변수 선언 및 입력:
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 보이는 색깔의 경우 True로 표기합니다.
visible = [False] * n

# 각 선분을 두 지점으로 나눠 담은 뒤,
# 정렬해줍니다.
# 이때 (x좌표, +1-1값, 선분 번호, y값)
# 형태로 넣어줍니다.
# +1은 시작점
# -1은 끝점을 뜻합니다.
points = []
for i in range(n):
    y, x1, x2 = segments[i]
    points.append((x1, +1, i, y)) # 시작점
    points.append((x2, -1, i, y)) # 끝점

# 정렬을 진행합니다.
points.sort()

# 각 점을 순서대로 순회합니다.
# 등장하고 아직 사라지지 않은
# 선분을 중 y값이 가장 작은 선분의 번호를 빠르게 구하기 위해
# treeset에
# (y값, 선분 번호) 형태로 넣어줍니다.
segs = SortedSet()
for _, v, index, y in points:
    # 시작점인 경우입니다.
    if v == +1:
        # 해당 선분 정보를 treeset에 넣어줍니다.
        segs.add((y, index))

    # 끝점인 경우입니다.
    else:
        # 해당 선분을 제거합니다.
        segs.remove((y, index))

    # 남아 있는 선분이 없다면 패스합니다. 
    if not segs:
        continue

    # 현재 눈에 보이는 선분을 찾아
    # 해당 index에 True값을 적어줍니다.
    _, target_index = segs[0]
    visible[target_index] = True

# 한 번이라도 보였던
# 선분의 개수를 세줍니다.
ans = 0
for i in range(n):
    if visible[i]:
        ans += 1

print(ans)