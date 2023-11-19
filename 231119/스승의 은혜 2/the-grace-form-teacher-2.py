n, b = map(int, input().split())
students = []
for _ in range(n):
    students.append(int(input())//2)
students = [0] + sorted(students)
cnt = 0
total = 0
for i in range(1, n+1):
    total += students[i-1] + students[i]
    if total > b:
        break
    cnt += 1
print(cnt)