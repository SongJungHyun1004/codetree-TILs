n = int(input())
cnt = 0
students = {
    'A': 0,
    'B': 0,
    'C': 0
}
pre = ['A','B','C']
for _ in range(n):
    c, s = input().split()
    students[c] += int(s)
    cur = [k for k, v in students.items() if max(students.values()) == v]
    if pre != cur:
        cnt += 1
        pre = cur
print(cnt)