an, bn = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
inter = len(a.intersection(b))
result = len(a)+len(b)-inter*2
print(result)