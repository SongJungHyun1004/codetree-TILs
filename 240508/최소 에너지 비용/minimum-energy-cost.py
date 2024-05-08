import sys
input = sys.stdin.readline

n = int(input())
energy_costs = list(map(int, input().split()))
charge_costs = list(map(int, input().split()))

min_cost = charge_costs[0]
total_cost = 0

# n-1까지 반복하는 이유는 마지막 장소에서는 이동하지 않기 때문
for i in range(n-1):
    # 현재 위치에서 다음 위치로 이동하는데 필요한 최소 비용 계산
    total_cost += min_cost * energy_costs[i]
    
    # 다음 위치의 충전 비용이 더 저렴하다면, 그 비용을 새로운 최소 비용으로 설정
    if charge_costs[i+1] < min_cost:
        min_cost = charge_costs[i+1]

print(total_cost)