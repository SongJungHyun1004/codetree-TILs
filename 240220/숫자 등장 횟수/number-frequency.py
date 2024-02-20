from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = Counter(arr)
m_lst = list(map(int, input().split()))
for i in m_lst:
    print(arr[i], end=' ')