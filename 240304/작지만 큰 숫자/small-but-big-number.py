from sortedcontainers import SortedSet
n, m = map(int, input().split())
s = SortedSet(list(map(int, input().split())))
m_lst = list(map(int, input().split()))
for i in m_lst:
    idx = s.bisect_right(i)-1
    if idx > -1:
        v = s[idx]
        print(v)
        s.remove(v)
    else:
        print(-1)