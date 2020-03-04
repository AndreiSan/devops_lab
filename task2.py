#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   2.0             2020           Final version
# --------------------------------------------------------------------


def differ(a, b):
    c = set(a)
    d = set(b)
    z = list(c & d)
    z = list(map(int, z))
    z.sort()  # Sort result list before output
    print(*z, sep=" ")


# Find common items in 2 lists without duplicates

a = input().split(" ")
b = input().split(" ")

differ(a, b)
