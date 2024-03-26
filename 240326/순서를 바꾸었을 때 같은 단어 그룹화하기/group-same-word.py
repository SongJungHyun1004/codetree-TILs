from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    word = ''.join(sorted(list(input())))
    dic[word] += 1
    
print(max(dic.values()))