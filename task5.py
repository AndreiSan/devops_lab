#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   1.0             2020           Initial version
# --------------------------------------------------------------------


def check(arg):
    """function to check if the number is self-dividing or not"""
    j = 0
    for i in arg:
        if (i != '0' and int(arg) % int(i) == 0):
            j += 1
        else:
            return "0"
    if j == len(arg):
        return arg
    else:
        return "0"


mas = input().split()
rez = []
n = int(mas[0])

while n <= int(mas[1]):
    if check(str(n)) != "0":
        rez.append(n)
    n += 1
print(rez)
