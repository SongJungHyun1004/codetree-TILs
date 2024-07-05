import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 번호별 그룹을 관리합니다.
uf = [0] * (n + 1)

# 현재 남아있는 칸의 개수는 n개입니다.
ans = n

# 초기 uf 값을 설정합니다.
for i in range(1, n + 1):
    uf[i] = i


# x의 대표 번호를 찾아줍니다.
def find(x):
    # x가 루트 노드라면 x값을 반환합니다.
    if uf[x] == x:
        return x
    # x가 루트 노드가 아니라면
    # x의 부모인 uf[x]에서 탐색을 더 진행한 뒤
    # 찾아낸 루트 노드를 uf[x]에 넣어줌과 동시에
    # 해당 노드값을 반환합니다.
    uf[x] = find(uf[x])
    return uf[x]


# m개의 칸 합치기 정보를 입력받습니다.
# 유니온 파인드를 통해 이미 합친 칸은 건너뜁니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
   
    while True:
        # x번 칸과 연결된 가장 큰 칸을 찾습니다.
        x = find(x)

        # 그 값이 y보다 크면 멈춥니다.
        if x >= y: 
            break

        # 그렇지 않다면 한칸씩 옆칸을 합칩니다.
        uf[x] = x + 1
        x = x + 1
        ans -= 1

    print(ans)