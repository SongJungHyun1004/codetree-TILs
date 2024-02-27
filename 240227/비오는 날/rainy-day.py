n = int(input())
closest = '9999-99-99'
for _ in range(n):
    date, weekday, weather = input().split()
    if weather == 'Rain':
        if closest > date:
            ans = [date, weekday, weather]
            closest = date
print(*ans)