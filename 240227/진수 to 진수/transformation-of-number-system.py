a, b = map(int, input().split())
n = input()
n = int(n, a)
result = ''
while n:
    result = str(n%b) + result
    n //= b
print(result)