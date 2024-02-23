import heapq
n = int(input())
lst = []
person = []
for i in range(1, n+1):
    s, e = map(int, input().split())
    person.append((s, e, i))
for s, e, i in person:
    lst.append((s, +1, i))
    lst.append((e, -1, i))
lst = sorted(lst)
cnt = 0
computers = []
user = {}
for _, v, i in lst:
    if v == +1:
        cnt += 1
        if computers:
            user[i] = heapq.heappop(computers)
        else:
            user[i] = cnt
    else:
        cnt -= 1
        c = user[i]
        heapq.heappush(computers, c)
user = sorted(user.items())
ans = [value for key, value in user]
print(*ans)