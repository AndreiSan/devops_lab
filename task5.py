#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   3.0             2020             Final version
# --------------------------------------------------------------------

a = list(map(int, input().split()))

mas = []

for i in range(a[0], a[1] + 1):
    current = i
    while current != 0:
        num = current % 10
        current //= 10
        if num == 0 or i % num != 0:
            break
    else:
        mas.append(i)
print(mas)
