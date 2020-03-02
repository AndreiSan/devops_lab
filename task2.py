#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   1.0             2020           Initial version
# --------------------------------------------------------------------


def differ(a, b):
    c = set(a)
    d = set(b)
    z = list(c & d)
    for i in range(len(z)):
        z[i] = int(z[i])
    z.sort()  # Sort result list before output
    print(z)
    print(*z, sep=" ")


# Find common items in 2 lists without duplicates

a = input("Your numbers sequence 1: ").split(" ")
b = input("Your numbers sequence 2: ").split(" ")

differ(a, b)
