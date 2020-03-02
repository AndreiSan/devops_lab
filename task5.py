#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   2.0             2020           Initial version
# --------------------------------------------------------------------

a = input().split()

mas = []

for i in range(int(a[0]), int(a[1]) + 1):
    flag = 0
    current = i
    while current != 0:
        num = current % 10
        current = int(current / 10)
        if num == 0 or i % num != 0:
            flag = 1
            break
    if flag == 0:
        mas.append(i)
print(mas)
