a, b = map(int, input().split())

def cal(a, b):
    if a < b:
        return min(a,b)+10, max(a,b)*2 
    else:
        return max(a,b)*2, min(a,b)+10

a, b = cal(a, b)
print(a, b)