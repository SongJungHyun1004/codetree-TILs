# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 번호별 그룹을 관리합니다.
uf = [0] * (n + 1)

# 각 그룹별 대응되는 반대팀 그룹을 관리합니다.
against = [0] * (n + 1)

# 모순이 있는지 여부를 저장합니다.
is_con = False

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


# x, y가 같은 집합이 되도록 합니다.
def union(x, y):
    # x, y의 대표 번호를 찾은 뒤
    # 연결해줍니다.
    X = find(x)
    Y = find(y)

    uf[X] = Y


# x, y는 반대팀의 집합이 되도록 합니다.
def beta(x, y):
    global is_con
    
    # x, y의 대표 번호를 찾은 뒤
    # 서로의 반대 집합으로 연산합니다.
    X = find(x)
    Y = find(y)

    # 둘이 같은 집합이면 모순입니다.
    if X == Y:
        is_con = True
        return
    
    if against[X]:
        union(against[X], Y)
    
    if against[Y]:
        union(against[Y], X)

    # 결합된 X와 Y의 신규 최종 노드번호를 찾고 반대팀으로 저장해줍니다.
    X2 = find(X)
    Y2 = find(Y)

    against[X2] = Y2
    against[Y2] = X2


# m개의 정보를 입력받습니다. 입력된 각각의 값은 서로 상대팀이 됩니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    beta(x, y)

if is_con:
    print(0)
else:
    print(1)