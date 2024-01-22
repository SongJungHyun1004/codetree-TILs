n, m, k = map(int, input().split())
dist_lst = list(map(int, input().split()))
arr = []
mx = 0
def get_score(arr):
    score = 0
    move = [1]*k
    for horse, dist in zip(arr, dist_lst):
        move[horse] += dist
    for i in move:
        if i >= m:
            score += 1
    return score

def choose(i):
    global mx
    if i > n:
        score = get_score(arr)
        mx = max(mx, score)
        return
    for nn in range(k):
        arr.append(nn)
        choose(i+1)
        arr.pop()

choose(1)
print(mx)