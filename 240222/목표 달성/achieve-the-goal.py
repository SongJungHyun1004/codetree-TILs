import sys

n, a, b, c, d = map(int, input().split())
min_energy = sys.maxsize

for i in range(n // a + 1):
    for j in range(n // c + 1):
        work_done = a * i + c * j
        energy = b * i + d * j
        if work_done >= n and energy < min_energy:
            min_energy = energy
            
print(min_energy)