n = int(input())
numbers = [float(input()) for _ in range(n)]

dp_min = [0]*n
dp_max = [0]*n
dp_min[0] = dp_max[0] = numbers[0]

for i in range(1, n):
    dp_min[i] = min(numbers[i], dp_min[i-1]*numbers[i], dp_max[i-1]*numbers[i])
    dp_max[i] = max(numbers[i], dp_min[i-1]*numbers[i], dp_max[i-1]*numbers[i])

print('%.3f' % max(dp_max))