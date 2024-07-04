# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))


def dist(i, j):
    return abs(fires[i] - stations[j])


def put_out_fire():
    # 화재 위치와 소방서 위치가
    # 가장 멀리 떨어져 있는 곳의 값을 계산해줍니다.
    max_dist = 0

    j = 1
    # 화재 가능성이 있는 위치들을 순서대로 보며
    # 더 가까이에 있는 소방서의 위치를 찾아 옮겨줍니다.
    for i in range(1, n + 1):
        # 현재 화재 가능성이 있는 위치에서
        # 현재 소방서의 위치보다
        # 그 다음 소방서의 위치가 더 가깝다면
        # 소방서의 위치를 계속 옮겨줍니다.
        while j + 1 <= m and dist(i, j) > dist(i, j + 1):
            j += 1
        
        # 화재 위치와 소방서 위치를 계산하여
        # 최댓값을 갱신해줍니다.
        max_dist = max(max_dist, dist(i, j))

    return max_dist


# 주어진 위치를 정렬해줍니다.
fires = [0] + sorted(fires)
stations = [0] + sorted(stations)

# 화재 진압에 필요한 최소 시간을 구해줍니다.
print(put_out_fire())