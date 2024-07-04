# 변수 선언 및 입력:
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0
points = []

# 주어진 좌표의 범위가 큰 경우에는
# 각 선분을 두 지점으로 나눠서
# +1, -1로 담은 뒤,
# 정렬해줍니다.
for x1, x2 in segments:
    points.append((x1, +1)) # 시작점
    points.append((x2, -1)) # 끝점

# 정렬을 진행합니다.
points.sort()

# 각 위치에 적혀있는 숫자들의 합을 구하면
# 매 순간마다 겹치는 구간의 횟수가 구해집니다.
# 이 중 최댓값을 구하면 됩니다.
sum_val = 0
for x, v in points:
    # 적혀있는 가중치를 전부 더해줍니다.
    sum_val += v

    # 최댓값을 갱신해줍니다.
    ans = max(ans, sum_val)

print(ans)