n = int(input())
board = list(map(int, input().split()))
pos_lst = []
mn = float('inf')
def choose(i):
    global mn
    v = board[i]
    if i == n-1:
        mn = min(mn, len(pos_lst))
        return
    for j in range(1, v+1):
        pos_lst.append(i+j)
        choose(i+j)
        pos_lst.pop()
choose(0)
if mn == float('inf'):
    mn = -1
print(mn)