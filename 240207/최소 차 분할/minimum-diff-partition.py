n = int(input())
numbers = list(map(int, input().split()))

dp = [0]*(sum(numbers)+1)
dp[0] = 1

for num in numbers:
    for i in range(sum(numbers), -1, -1):
        if dp[i]:
            dp[i+num] = 1

min_diff = float('inf')
total_sum = sum(numbers)

for i, can_make in enumerate(dp):
    if can_make:
        group1 = i
        group2 = total_sum - i
        min_diff = min(min_diff, abs(group1 - group2))

print(min_diff)