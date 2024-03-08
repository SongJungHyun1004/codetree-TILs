n = int(input())
init_string = list(input())[::-1]
final_string = list(input())[::-1]
cnt = 0
for i in range(n):
    if init_string[i] != final_string[i]:
        cnt += 1
        for j in range(i, n):
            if init_string[j] == 'G':
                init_string[j] = 'H'
            else:
                init_string[j] = 'G'
print(cnt)