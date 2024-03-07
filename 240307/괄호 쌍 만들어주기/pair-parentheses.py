a = list(input())
open = 0
close = 0
for i in range(len(a)-1):
    string = ''.join(a[i:i+2])
    if '((' == string:
        open += 1
    elif '))' == string:
        close += 1
print(open*close)