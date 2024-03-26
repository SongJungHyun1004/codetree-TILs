from collections import Counter
string = Counter(list(input()))
for s, freq in string.items():
    if freq == 1:
        print(s)
        exit(0)
print('None')