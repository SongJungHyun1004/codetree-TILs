a, b = map(int, input().split())

def cal(a, b):
    return min(a,b)+10, max(a,b)*2

a, b = cal(a, b)
print(a, b)