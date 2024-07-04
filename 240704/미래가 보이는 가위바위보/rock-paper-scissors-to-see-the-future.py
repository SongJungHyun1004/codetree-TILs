# 변수 선언 및 입력:
n = int(input())
matches = [input() for _ in range(n)]

L, R = [0] * n, [0] * n
ans = 0

# L 배열을 채워줍니다.
# L[i] = 0번부터 i번까지 동일한 모양만 냈을 때
#        최대로 이길 수 있는 횟수
for shape in "PHS":
    same_cnt = 0
    for i in range(n):    
        if matches[i] == shape:
            same_cnt += 1
        
        L[i] = max(L[i], same_cnt)

# R 배열을 채워줍니다.
# R[i] = i번부터 n - 1번까지 동일한 모양만 냈을 때
#        최대로 이길 수 있는 횟수

for shape in "PHS":
    same_cnt = 0
    for i in range(n - 1, -1, -1):
        if matches[i] == shape:
            same_cnt += 1
        
        R[i] = max(R[i], same_cnt)

# 해당 순간에 선택을 변경했다 했을 때
# 최대로 이기는 횟수를 갱신해줍니다.
for i in range(0, n - 1):
    ans = max(ans, L[i] + R[i + 1])

print(ans)