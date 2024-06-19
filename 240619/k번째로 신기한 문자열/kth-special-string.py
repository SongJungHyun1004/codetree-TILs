n, k, T = input().split()
n, k = int(n), int(k)
words_lst = []
for _ in range(n):
    word = input()
    if len(T) <= len(word) and word[:len(T)] == T:
        words_lst.append(word)
words_lst.sort()
print(words_lst[k-1])