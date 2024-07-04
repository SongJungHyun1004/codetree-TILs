# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
L = [0] * (m + 2)
R = [0] * (m + 2)

# L 배열을 채워줍니다.
# L[i] = 수열 B의 1번부터 i번까지 1 -> i 순서대로
#        수열 A의 왼쪽부터 순서대로 매칭헀을 때 
#        마지막으로 매칭되는 수열 A 원소의 위치
i = 1
for j in range(1, m + 1):
    while i <= n and A[i] != B[j]: 
        i += 1
    L[j] = i
    if i <= n: 
        i += 1

# R 배열을 채워줍니다.
# R[i] = 수열 B의 n번부터 i번까지 n -> i 순서대로
#        수열 A의 오른쪽부터 순서대로 매칭헀을 때 
#        마지막으로 매칭되는 수열 A 원소의 위치
i = n
for j in range(m, 0, -1):
    while i >= 1 and A[i] != B[j]:
        i -= 1
    R[j] = i
    if i >= 1: 
        i -= 1

# 경계 부분 처리를 위해 적절한 값을 넣어줍니다.
L[0] = 0
R[m + 1] = n + 1

# 수열 B의 j번 원소를 지웠다고 했을 때
# L[j - 1] < R[j + 1]을 만족한다면
# 매칭이 가능하다는 것이므로 그 개수를 세줍니다.
ans = 0
for j in range(1, m + 1):
    if L[j - 1] < R[j + 1]: 
        ans += 1

print(ans)