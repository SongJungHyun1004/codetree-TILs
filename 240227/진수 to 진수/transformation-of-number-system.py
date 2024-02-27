a, b = map(int, input().split())
n = input()
n = int(n, a)
dic = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}
result = ''
while n:
    result = dic[n%b] + result
    n //= b
print(result)