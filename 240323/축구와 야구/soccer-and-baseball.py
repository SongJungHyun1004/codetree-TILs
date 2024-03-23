n = int(input())
players = []
for _ in range(n):
    s, b = map(int, input().split())
    players.append((s, b))

# 축구 능력과 야구 능력의 차이를 기준으로 정렬
players.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)

# 축구팀과 야구팀의 능력 합
soccer_sum, baseball_sum = 0, 0

# 축구팀과 야구팀에 선수 할당
soccer_count, baseball_count = 0, 0
for s, b in players:
    # 축구팀이나 야구팀 중 어디에 할당할지 결정
    if (s > b and soccer_count < 11) or baseball_count == 9:
        soccer_sum += s
        soccer_count += 1
    else:
        baseball_sum += b
        baseball_count += 1

# 결과 출력
print(soccer_sum + baseball_sum)