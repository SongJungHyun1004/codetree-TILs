n = int(input())

def upside_down_star(i):
    if i == 0:
        return
    print('* '*i)
    upside_down_star(i-1)

def star(i):
    if i == n:
        return
    print('* '*(i+1))
    star(i+1)

upside_down_star(n)
star(0)